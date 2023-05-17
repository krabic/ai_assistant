from langchain.prompts.prompt import PromptTemplate

_template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that please contact 
with support by email support@nifty-bridge.com, don't try to make up an answer.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
NIFTY_BRIDGE_PROMPT = PromptTemplate.from_template(_template)

prompt_template = """
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that please contact with 
support by email support@nifty-bridge.com, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:"""

QA_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
