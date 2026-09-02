import streamlit as st
from google import genai
from google.genai import types

# 1. Page Configuration & Aesthetic UI Styling
st.set_page_config(
    page_title="SecureMind AI", 
    page_icon="🛡️", 
    layout="centered"
)

st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; }
    .main-title { font-size: 2.2rem; font-weight: 700; color: #1e293b; text-align: center; margin-bottom: 0.5rem; }
    .sub-title { font-size: 1.1rem; color: #64748b; text-align: center; margin-bottom: 2rem; }
    </style>
""", unsafe_index=True)

st.markdown('<div class="main-title">🛡️ SecureMind AI</div>', unsafe_index=True)
st.markdown('<div class="sub-title">Empathetic Technical Support & Grounding Assistant</div>', unsafe_index=True)

# 2. Secure API Key Management
# Users can input their key in the sidebar securely
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Enter Google Gemini API Key:", type="password")
    st.markdown("---")
    st.markdown("**Project Scope:** Built for handling cybersecurity anxieties with clear technical facts and empathetic grounding.")

# 3. Initialize Conversation History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat logs on screen refresh
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Advanced System Prompt Engineering (Core AI Persona)
SYSTEM_PROMPT = """
You are SecureMind AI, a compassionate technical assistant designed to help users navigate digital security anxieties and cyber-phobias (e.g., fears of SIM cloning, device tapping, or remote hacking).

Your conversational framework must strictly adhere to these architectural rules:
1. EMPATHY FIRST: In your very first sentence, authentically validate the user's emotional state or worry. Never dismiss their fear as irrational.
2. TECHNICAL SIMPLIFICATION: Explain complex telecom or computing concepts (like network routing, IMSI/IMEI tracking, encryption, or TRAI/GSMA protocols) using clear, universal, non-technical language. 
3. STRATEGIC SCANNABILITY: Break long blocks of text into highly scannable bullet points, tables, or numbered lists. Use markdown bolding on critical safety terms or definitive proofs.
4. GROUNDING WORKFLOWS: Provide immediate, actionable, physical validation steps the user can execute on their physical device to check reality (e.g., dial codes, checking system status menus).
5. NETWORK CERTAINTY: Reassure the user with logical network laws (e.g., 'If your device has live service bars and says connected, it is a mathematical certainty that a cloned version is not active elsewhere').
6. SAFETY LIFELINE: If the user indicates extreme psychological distress, gently and neutrally advise them to speak to a licensed mental health professional, while keeping your primary focus on technical clarification.
"""

# 5. Core Chat Handling & Logic Execution
if prompt := st.chat_input("How can I help you feel secure today?"):
    # Render user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Verify API credentials before processing
    if not api_key:
        st.warning("Please insert your Google Gemini API Key in the left sidebar to start the assistant.")
    else:
        try:
            # Initialize the modern Google GenAI Client
            client = genai.Client(api_key=api_key)
            
            # Format the full context of the conversation for the API
            formatted_contents = []
            for msg in st.session_state.messages:
                role = "user" if msg["role"] == "user" else "model"
                formatted_contents.append(
                    types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])])
                )
            
            # Streaming response wrapper for optimal user experience
            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                full_response = ""
                
                # Execute API Call using recommended gemini-2.5-flash model
                response_stream = client.models.generate_content_stream(
                    model='gemini-2.5-flash',
                    contents=formatted_contents,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.4 # Lower temperature reduces hallucinations and ensures consistent facts
                    )
                )
                
                for chunk in response_stream:
                    full_response += chunk.text
                    response_placeholder.markdown(full_response + "▌")
                
                response_placeholder.markdown(full_response)
            
            # Save assistant response to state
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"An error occurred while connecting to the AI: {str(e)}")
  
