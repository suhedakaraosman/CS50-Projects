import os
from openai import OpenAI

def forge_stealth_uplink():
    stealth_token = os.environ.get("GROQ_API_KEY")

    if not stealth_token:
        raise ValueError("Kimlik dogrulama basarisiz! GROQ_API_KEY bulunamadi.")

    uplink_node = OpenAI(
        api_key=stealth_token,
        base_url="https://api.groq.com/openai/v1"
    )
    return uplink_node

def ignite_dynamic_exchange(uplink_node):
    user_inquiry = input("Prompt: ")
    directive_rule = "Limit your answer to one sentence."
    ai_yield = uplink_node.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": directive_rule},
            {"role": "user", "content": user_inquiry}
        ]
    )

    print(ai_yield.choices[0].message.content)

active_gateway = forge_stealth_uplink()
ignite_dynamic_exchange(active_gateway)
