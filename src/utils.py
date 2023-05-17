from langchain.text_splitter import NLTKTextSplitter
from langchain.document_loaders import PyPDFLoader
from fastapi import HTTPException, Depends
from config import X_API_Key
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")


class LoadPdf:
    def __init__(self):
        self.load = None
        self.loader_pdf = None

    def load_pdf(self, file_path):
        self.loader_pdf = PyPDFLoader(file_path)
        self.load = str(self.loader_pdf.load())
        return self.load


class TransformData:
    def __init__(self):
        self.text_splitter = None

    def pdf_to_llm_chunks(self, load: str):
        self.text_splitter = NLTKTextSplitter()
        chunks_for_llm = self.text_splitter.split_text(load)
        return chunks_for_llm


def check_api_key(api_key: str = Depends(api_key_header)):
    if api_key != X_API_Key:
        raise HTTPException(status_code=403, detail="Invalid API key")
    else:
        return True
