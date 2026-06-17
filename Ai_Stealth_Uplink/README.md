# 🕵️‍♂️ CS50 - AI Stealth Uplink
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Groq](https://img.shields.io/badge/Groq-f55036?style=for-the-badge&logo=groq&logoColor=white)
![Meta Llama 3](https://img.shields.io/badge/Meta_Llama_3-0466C8?style=for-the-badge)
## 📜 About The Project
This project is a terminal-based AI chat application initially inspired by the CS50 curriculum. However, it features a custom-engineered architecture designed to bypass API costs while delivering state-of-the-art performance.
## 🎓 CS50 Context: Why Not OpenAI?
The standard CS50 curriculum utilizes the official OpenAI API, which operates on a pay-per-query model. To make this project **100% free, sustainable, and open-source**, a strategic architectural pivot was made:
* **The Workaround:** The project still uses the `openai` Python client (as taught in CS50), but ingeniously redirects the base URL to the Groq API infrastructure.
* **The Engine:** Instead of closed-source GPT models, it runs Meta's `Llama-3.3-70b-versatile`.
* **The Result:** Ultra-low latency inference with zero API costs.
## 🏗️ Technical Architecture
* **Model:** `Llama-3.3-70b-versatile`
* **Infrastructure:** Groq API 
* **Development Environment:** Linux/WSL (Ubuntu)
* **Security:** API keys are strictly isolated via environment variables.
## 🚀 Installation & Usage
1. **Obtain your API key:** Get your free key from the [Groq Console](https://console.groq.com/).
2. **Set up the environment and run:**
```bash
export GROQ_API_KEY='your_api_key_here'
python3 -m venv venv
source venv/bin/activate
pip install openai
python3 chat.py
