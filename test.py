import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_gpt_response(user_query):
    endpoint = "https://umesh-mltkh465-eastus2.openai.azure.com/openai/v1"
    deployment_name = "gpt-5.2-chat"
    api_key = os.getenv("AZURE_OPENAI_KEY")
    if not api_key:
        raise RuntimeError("Set AZURE_OPENAI_KEY before calling the Azure OpenAI service.")

    client = OpenAI(
        base_url=endpoint,
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {
                "role": "user",
                "content": user_query,
            }
        ],
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    response = get_gpt_response("What is the leave policy?")
    print(response)
