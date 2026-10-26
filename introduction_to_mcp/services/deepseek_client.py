import httpx

from src.config import settings


class DeepSeekClient:
    async def chat(self, prompt: str, model: str | None = None):
        model = model or settings.DEFAULT_MODEL
        headers = {
            "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.DEEPSEEK_BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
                timeout=120,
            )
        response.raise_for_status()
        return response.json()


deepseek_client = DeepSeekClient()
