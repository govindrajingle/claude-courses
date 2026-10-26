import asyncio
from src.services.deepseek_client import deepseek_client


async def main():
    response = await deepseek_client.chat("reply with exactly: connection successful")
    print(response)


asyncio.run(main())
