# ------------------------------------------------------------
# Importing required LangGraph and LangChain components
# ------------------------------------------------------------

# START, END → special markers for beginning and end of the graph
# StateGraph → used to build the workflow graph
# MessagesState → built‑in LangGraph state for storing conversation messages
from langgraph.graph import START, END, StateGraph, MessagesState

# ChatOpenRouter → LLM wrapper to call OpenRouter models
from langchain_openrouter import ChatOpenRouter

# InMemorySaver → stores conversation history (memory) for the agent
from langgraph.checkpoint.memory import InMemorySaver

# BaseMessage → generic message type
# HumanMessage → message coming from the user
from langchain_core.messages import BaseMessage, HumanMessage

# load_dotenv → loads environment variables from .env file
from dotenv import load_dotenv

# Load environment variables (like OPENROUTER_API_KEY)
load_dotenv()


# ------------------------------------------------------------
# Initialize the LLM (OpenRouter model)
# ------------------------------------------------------------
llm = ChatOpenRouter(
    model="gpt-4o-mini"   # The model you want to use
)


# ------------------------------------------------------------
# Define the chatbot node (function)
# This is the actual logic that runs inside the graph
# ------------------------------------------------------------
def ChatbotNode(state: MessagesState) -> MessagesState:
    # Send the accumulated messages to the LLM and get a response
    result = llm.invoke(state["messages"])

    # Return the new state containing the LLM's reply
    # LangGraph will automatically append this to the message history
    return {'messages': [result]}


# ------------------------------------------------------------
# Build the LangGraph workflow
# ------------------------------------------------------------

# Create a graph that uses MessagesState (built‑in message container)
graph = StateGraph(MessagesState)

# Add the chatbot node to the graph
graph.add_node('ChatbotNode', ChatbotNode)

# Connect START → ChatbotNode → END
graph.add_edge(START, 'ChatbotNode')
graph.add_edge('ChatbotNode', END)

# Compile the graph with memory enabled
workflow = graph.compile(checkpointer=InMemorySaver())


# ------------------------------------------------------------
# OPTIONAL: Generate a Mermaid diagram of the graph
# (You commented this out, but it shows the graph visually)
# ------------------------------------------------------------
# image = workflow.get_graph().draw_mermaid_png()
# with open("chatbot_graph.png", mode="wb") as f:
#     f.write(image)


# ------------------------------------------------------------
# Chat Loop — keeps asking user for input until "exit"
# ------------------------------------------------------------
while True:
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        break

    # Invoke the workflow with the user's message
    response = workflow.invoke(
        {'messages': HumanMessage(content=user_input)},
        config={'configurable': {'thread_id': 1}}  # memory thread ID
    )

    # Print the chatbot's reply (last message)
    print(response['messages'][-1].content)