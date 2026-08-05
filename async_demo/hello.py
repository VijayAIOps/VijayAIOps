from groq import AsyncGroq
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

request = AsyncGroq(api_key=os.getenv("api_key_value"))
if request.api_key !=None:
    print("API key is set correctly")


async def ask(prompts):
  response = await request.chat.completions.create(
        model="LLaMA-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompts}
        ]
    )
if response.choices:
        return response.choices[0].message.content

async def main():
    prompts =["what is the latest version of iphone","what is the value of 5*5","Tell me a joke","who is india prime minister"]


