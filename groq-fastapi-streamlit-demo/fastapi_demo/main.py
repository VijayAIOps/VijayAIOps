from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


api_key = os.getenv("api_key_value")
print("post key...")

if not api_key:
    raise ValueError("Groq API key is not set. Please add it to your .env variables")

client = Groq(api_key=api_key)
print("APIKEY:", api_key)

class RequestModel(BaseModel):
    name: str

#demonstrate LLM response for API request call.
class PromptRequest(BaseModel):
    print("inside prompt request...")
    message:str

class PromptResponse(BaseModel):
    print("inside prompt response...")
    message:str
    model:str
    status:str

@app.post("/prompt")
def send_prompt(request: PromptRequest):
    print("request received:", request.message)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
                messages=[{"role":"user",
                                    "content":request.message
                                    }]
        )
    return PromptResponse(
        message=response.choices[0].message.content,
        model="llama-3.3-70b-versatile",
        status="success"
    )


@app.get("/")
def show():
    return "Hello from fastapi-demo!"

@app.get("/products")
def get_products():
    return {"name":"iphone","price":"25000"}

@app.get("/login")
def login():
    return {"message":"login successful"}

#demonstrate post request using thunder client
@app.post("/generate")
def generate(request: RequestModel):
    return f"welcome {request.name}"



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="localhost",port=8000,reload=True)
    
