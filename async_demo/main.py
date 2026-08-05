from groq import AsyncGroq
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

client = AsyncGroq(api_key=os.getenv("api_key_value"))


async def ask(prompt):
    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


async def main():

    prompts = ["Tell me a joke", "What is the capital of India", "What is 2+2"]

    results = await asyncio.gather(*(ask(p) for p in prompts))
    for r in results:
        print(r)

asyncio.run(main())
