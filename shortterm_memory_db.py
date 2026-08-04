from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langgraph.checkpoint.postgres import PostgresSaver
import os

load_dotenv()

llm = ChatOpenRouter(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY")

)

DB_URI = "postgresql://postgres:welcome@localhost:5432/conversationdb?sslmode=disable"
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup()

    agent = create_agent(model=llm,
                        system_prompt="""
                        You are an AI chat assistant who answers queries with a bit of humor.Use emojis to decorate your message.Be polite and professional.
                        """,
                        checkpointer = checkpointer
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
