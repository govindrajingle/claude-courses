from src.services.deepseek_client import deepseek_client


async def execute(prompt: str):
    response = await deepseek_client.chat(prompt)
    return response["choices"][0]["messages"]["content"]
