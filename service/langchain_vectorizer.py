# -*- coding: UTF-8 -*-
from pathlib import Path

from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch


class Vectorizer:
    def __init__(self):
        pass

    def get_vector(self, path: Path) -> list:
        loader = TextLoader(str(path))
        data = loader.load()

        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000, chunk_overlap=0
        )
        documents = text_splitter.split_documents(data)
        embeddings = OpenAIEmbeddings()
        db = ElasticVectorSearch.from_documents(
            documents,
            embeddings,
            elasticsearch_url="http://localhost:9200/",
            index_name="zhanglei-test",
        )
        print(db.client.info())
