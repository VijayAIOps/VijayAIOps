from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

import os

load_dotenv()

model = ChatOpenRouter(model=os.getenv("MODEL"))
conversation_history=[]

while True:
    user_input = input("you: ")
    conversation_history.append(user_input)
    if user_input.lower() == "exit":
        break    
    
    response = model.invoke(conversation_history)
    conversation_history.append(response.content)    
    print(f"bot: {response.content}")

#print(f"conversation history : {conversation_history}")
