# 🛡️ SecureMind AI: Empathetic GenAI Assistant for Cyber-Anxiety

SecureMind AI is a specialized conversational application engineered to support individuals experiencing technology-related anxieties or cyber-phobias (such as fears of SIM cloning, phone wiretapping, or device hacking). 

Unlike rigid tech support bots, this assistant utilizes **Cognitive Grounding Frameworks** combined with **deterministic network security logic** to de-escalate anxiety while guiding users through physical device security verification.

## 🛠️ Tech Stack & Architecture
- **Language:** Python 3.10+
- **LLM Core Engine:** Google Gemini Pro (`gemini-2.5-flash`) via the modern Google GenAI Client
- **Orchestration & Web Interface:** Streamlit (leveraging component session states for chat preservation)
- **Prompt Engineering:** Strict system context architecture with strict guardrails against clinical/medical hallucinations.

## ⚙️ How It Works (Core Features)
1. **Empathy-First Protocol:** Automatically validates user distress prior to delivering technical analyses.
2. **Technical Simplification Engine:** Translates complex cellular telecom routing, GSM cloning hardware protocols, and GSMA blacklisting laws into accessible English.
3. **Device-Level Grounding Checklists:** Generates concrete verification tasks (e.g., checking cellular network states, executing IMEI `*#06#` diagnostic routines).

## 🚀 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com
   cd securemind-ai
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
4. Securely enter your Google Gemini API Key into the application sidebar interface to activate the LLM instance.
5. 
