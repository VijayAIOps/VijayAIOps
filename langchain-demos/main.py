from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(model=os.getenv("MODEL"))

response = model.invoke("what is capital of india")
print(response.content)



def main():
    print("Hello from langchain-demos!")


if __name__ == "__main__":
    main()
