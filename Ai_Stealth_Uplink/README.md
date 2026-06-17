CS50 - AI Stealth Uplink
This project is a high-efficiency AI interface running via terminal, powered by the Groq API. It provides rapid and secure access to state-of-the-art open-source Llama models, bypassing the traditional constraints of closed-source AI services.

Technical Architecture
The system uses the openai Python client as a bridge to communicate with Llama models through the Groq infrastructure.

Model: Llama-3.3-70b-versatile

Infrastructure: Groq API (Low-latency inferencing)

Development Environment: Linux/WSL (Ubuntu)

Security: API keys are isolated via environment variables to ensure professional security standards.

Why Llama?
Instead of closed-source OpenAI models, Llama 3.3 was selected for this project due to:

Open-Source Philosophy: We believe in the power of transparent and modifiable models.

Performance: Ultra-low latency provided by Groq's optimized hardware.

Cost-Efficiency: Providing a sustainable and cost-effective solution for AI-powered development.

Installation
Obtain your API key: Groq Console

Export your API key as an environment variable:

Bash
export GROQ_API_KEY='your_api_key_here'
Set up your virtual environment and run the script:

Bash
python3 -m venv venv
source venv/bin/activate
pip install openai
python3 chat.py