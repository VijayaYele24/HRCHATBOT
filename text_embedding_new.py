import os
from dotenv import load_dotenv
load_dotenv()
from openai import AzureOpenAI
API_KEY = os.getenv("AZURE_OPENAI_KEY")
def get_embedding(text):
    import os
    from openai import AzureOpenAI

    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    model_name = "text-embedding-3-small"
    deployment = "text-embedding-3-small"

    api_version = "2024-02-01"

    client = AzureOpenAI(
        api_version="2024-12-01-preview",        
        api_key=API_KEY
    )
    response = client.embeddings.create(
        input=["first phrase","second phrase","third phrase"],
        model=deployment
    )

    for item in response.data:
        length = len(item.embedding)
        print(
            f"data[{item.index}]: length={length}, "
            f"[{item.embedding[0]}, {item.embedding[1]}, "
            f"..., {item.embedding[length-2]}, {item.embedding[length-1]}]"
        )
    print(response.usage)


if __name__ == "__main__":
    text = "What are the leave policies?"
    embedding = get_embedding(text)
    print(embedding)