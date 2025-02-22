import sys
__import__('pysqlite3')
import pysqlite3
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import os
from langchain_openai import OpenAIEmbeddings
from typing import List
from langchain_core.documents import Document
from uuid import uuid4
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings



class DocumentLoader:
    def __init__(self, model="all-MiniLM-L6-v2", collection_name="rag-podcast-poc", persist_directory="./chroma_langchain_db"):
        
        if model == 'text-embedding-3-small':
            self.embeddings = OpenAIEmbeddings(model=model, openai_api_key=os.getenv("OPENAI_API_KEY"))
        else:
            self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        self.collection_name = collection_name
        self.persist_directory = persist_directory
        
        self.vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=persist_directory
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=150,
            length_function=len,
            is_separator_regex=False,
        )

    def load_documents(self, path: str) -> List[Document]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"The specified path does not exist: {path}")
        
        docs = []
        ii = 1
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r', encoding='latin-1') as f:
                content = f.read()
            contents = self.text_splitter.create_documents([content])
            for chunkid, content in enumerate(contents):
                docs.append(Document(
                    page_content=f"{content}",
                    metadata={"date": file[:10], "segment": file.split('-')[-1][:-4], "chunk": chunkid+1},
                    id=ii,
                ))
                ii += 1
        return docs

    def load_documents_into_database(self, folder_path="data/data-news"):
        if not os.path.exists(self.persist_directory) or len(os.listdir(self.persist_directory)) < 2:
            documents = self.load_documents(folder_path)
            uuids = [str(uuid4()) for _ in range(len(documents))]
            self.vector_store.add_documents(documents=documents, ids=uuids)
        return self.vector_store