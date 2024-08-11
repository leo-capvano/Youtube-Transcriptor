from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

TEMPERATURE = 0
MODEL_NAME = "gpt-3.5-turbo"

load_dotenv()


def get_llm_chain():
    prompt_template = """Write a summary of the following:
    "{text}"
    CONCISE SUMMARY:"""
    prompt = PromptTemplate.from_template(prompt_template)
    llm = ChatOpenAI(temperature=TEMPERATURE, model_name=MODEL_NAME)
    return LLMChain(llm=llm, prompt=prompt)
