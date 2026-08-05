from langchain_openrouter import ChatOpenRouter
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)

conversation_history=[
    SystemMessage(content="""
    You are a helpful AI assistant who answers queries with a bit of humour. Use emojis to make your response looks attractive. Give friendly answers while maintaining the professional tone.
    """)
]

while True:
    user_input = input("You: ")
    conversation_history.append(HumanMessage(content=user_input))
    if user_input.lower()=="exit":
        break
    response = model.invoke(conversation_history)
    conversation_history.append(AIMessage(content=response.content))
    print(response.content)

print(conversation_history)