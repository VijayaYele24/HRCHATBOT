import os

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()


def get_gpt_response(user_query):
    endpoint = "https://umesh-mlubxbd0-eastus2.cognitiveservices.azure.com/"
    model_name = "gpt-4.1"
    deployment = "gpt-4.1"

    subscription_key = os.getenv("AZURE_OPENAI_KEY")
    if not subscription_key:
        raise RuntimeError("Set AZURE_OPENAI_KEY before calling the Azure OpenAI service.")
    api_version = "2024-12-01-preview"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "I am going to Paris, what should I see?",
            }
        ],
        max_completion_tokens=13107,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model=deployment
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    response = get_gpt_response("What is the leave policy?")
    print(response)
