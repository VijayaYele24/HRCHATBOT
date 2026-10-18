import os

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()


def get_embedding(text):
    endpoint = "https://instancechatbot.openai.azure.com/"
    model_name = "text-embedding-ada-002"
    deployment = "text-embedding-ada-002"

    api_key = os.getenv("AZURE_OPENAI_KEY")
    if not api_key:
        raise RuntimeError("Set AZURE_OPENAI_KEY before calling the Azure OpenAI service.")

    client = AzureOpenAI(
        api_version="2024-12-01-preview",
        azure_endpoint=endpoint,
        api_key=api_key,
    )

    response = client.embeddings.create(
        input=["first phrase", "second phrase", "third phrase"],
        model=deployment,
    )

    for item in response.data:
        length = len(item.embedding)
        print(
            f"data[{item.index}]: length={length}, "
            f"[{item.embedding[0]}, {item.embedding[1]}, "
            f"..., {item.embedding[length - 2]}, {item.embedding[length - 1]}]"
        )
        print(response.usage)
    return response.data[0].embedding


if __name__ == "__main__":
    text = "What are the leave policies?"
    embedding = get_embedding(text)
    print(embedding)
