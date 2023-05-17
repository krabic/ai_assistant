from fastapi import FastAPI, Request
from utils import check_api_key
from prompt import NIFTY_BRIDGE_PROMPT
from utils import LoadPdf, TransformData
from vector_provider import VectorStoreProvider
from config import FILE_PATH
import nltk


nltk.download('punkt')
loadPdf = LoadPdf()
transform_data = TransformData()
vector_store_provider = VectorStoreProvider()

chunks = transform_data.pdf_to_llm_chunks(loadPdf.load_pdf(FILE_PATH))

vector_store_provider.init_embeddings(chunks)

vector_store_provider.add_chat_history()
vector_store_provider.search_docstring(NIFTY_BRIDGE_PROMPT)


ai_assistant_api = FastAPI()


@ai_assistant_api.post("/api/send")
def create_answer(request: Request, question: str):
    api_key = request.headers.get('api_key')
    if check_api_key(api_key):
        response = vector_store_provider.docsearch({"question": question})
        return {"response": response["answer"]}
    else:
        return {"error 403": "Invalid API key"}
