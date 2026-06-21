from openai import OpenAI
from config import get_provider_config
from prompt import build_prompt

config = get_provider_config()

client = OpenAI(
    api_key=config["api_key"],
    base_url=config["base_url"]
)

def generate_sql(question):

    prompt = build_prompt(question)

    response = client.chat.completions.create(
        model=config["model"],
        messages=[
            {
                "role": "system",
                "content": "You are an expert SQL developer. Return ONLY SQL."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content