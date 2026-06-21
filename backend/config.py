# config.py

import os
from dotenv import load_dotenv

load_dotenv()


def get_provider_config():

    provider = os.getenv(
        "AI_PROVIDER",
        "groq"
    ).lower()

    providers = {

        "openai": {
            "api_key":
                os.getenv(
                    "OPENAI_API_KEY"
                ),

            "base_url":
                "https://api.openai.com/v1",

            "model":
                os.getenv(
                    "OPENAI_MODEL"
                )
        },

        "groq": {
            "api_key":
                os.getenv(
                    "GROQ_API_KEY"
                ),

            "base_url":
                "https://api.groq.com/openai/v1",

            "model":
                os.getenv(
                    "GROQ_MODEL"
                )
        },

        "ollama": {
            "api_key":
                os.getenv(
                    "OLLAMA_API_KEY"
                ),

            "base_url":
                "http://localhost:11434/v1",

            "model":
                os.getenv(
                    "OLLAMA_MODEL"
                )
        }
    }

    return providers[provider]