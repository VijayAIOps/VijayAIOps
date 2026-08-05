from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)

template = PromptTemplate(template="Write an article on the concept of {topic}.")
template2 = PromptTemplate(template="Write 5 MCQ based questions with answers based on the below article: \n {article}")

# prompt1 = template.invoke({'topic':'AI'})
# prompt2 = template.invoke({'topic': 'CyberSecurity'})

# response = model.invoke(prompt1)

# print(response.content)

chain = template | model | StrOutputParser() | template2 | model | StrOutputParser()

print(chain.invoke({'topic': 'Cyber Security'}))