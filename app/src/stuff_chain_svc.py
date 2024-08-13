from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain


def generate_summary(stuff_llm_chain: LLMChain, doc_variable_name: str, document):
    stuff_chain = StuffDocumentsChain(llm_chain=stuff_llm_chain, document_variable_name=doc_variable_name)
    return stuff_chain.invoke(document)["output_text"]
