import os
import asyncio
import aiohttp
import json

async def get_response(message):
    async with aiohttp.ClientSession() as session:
        api_key = os.environ.get("OPENAI_API_KEY")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "prompt": message,
            "temperature": 0.5,
            "max_tokens": 100,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        url = "https://api.openai.com/v1/engines/davinci/jobs"
        async with session.post(url, headers=headers, data=json.dumps(data)) as resp:
            response_text = await resp.text()
            response_json = json.loads(response_text)
            return response_json["choices"][0]["text"]

# Bot Telegram Code Here
