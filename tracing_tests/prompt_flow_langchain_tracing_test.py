from promptflow.tracing import start_trace

from opentelemetry.instrumentation.langchain import LangchainInstrumentor

import os

from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# start a trace session, and print a url for user to check trace
start_trace()

# enable langchain instrumentation


instrumentor = LangchainInstrumentor()
if not instrumentor.is_instrumented_by_opentelemetry:
    instrumentor.instrument()



llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}"),
    ]
)

chain = LLMChain(llm=llm, prompt=prompt, output_key="metrics")
chain({"input": "What is ChatGPT?"})