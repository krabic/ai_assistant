from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from config import OPENAI_API_KEY


class VectorStoreProvider:
    def __init__(self):
        self.db_vector = None
        self.memory = None
        self.docsearch = None
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.chat_open_ai = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.8,
                                       model_name="gpt-3.5-turbo")

    def init_embeddings(self, data):
        self.db_vector = Chroma.from_texts(data, self.embeddings, persist_directory="data")
        self.db_vector.persist()

    def add_chat_history(self):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        return self.memory

    def search_docstring(self, prompt):
        self.docsearch = ConversationalRetrievalChain.from_llm(
            self.chat_open_ai,
            self.db_vector.as_retriever(),
            condense_question_prompt=prompt,
            memory=self.memory
        )
        return self.docsearch
