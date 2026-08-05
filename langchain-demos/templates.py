from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

import os

load_dotenv()

model = ChatOpenRouter(
    model= os.getenv("MODEL")
)

template = PromptTemplate(template="write an article in the concept of {topic}")

prompt1 = template.invoke({"topic": "AI"})
prompt2 = template.invoke({"topic": "Machine Learning"})
response = model.invoke(prompt1)
print(response.content)

#chain = template | model | StrOutputParser()#LCEL
#print(chain.invoke({"topic":"AI"}))


