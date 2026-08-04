from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
import os

load_dotenv()

llm = ChatOpenRouter(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY")

)

agent = create_agent(model=llm,
                     system_prompt="""
                     You are an AI chat assistant who answers queries with a bit of humor.Use emojis to decorate your message.Be polite and professional.
                     """,
                     checkpointer = InMemorySaver()
)   

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = agent.invoke(
        {
            "messages": [
                { "role" : "user", "content" : user_input }
                
                ]
        },config={"configurable": {"thread_id" :1}}
    )
    print(response["messages"][-1].content)
