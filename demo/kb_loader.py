# kb_loader.py
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

loader = PyPDFLoader("docs/MicroVec User's Manual.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

emb = OpenAIEmbeddings()
vectordb = Chroma.from_documents(chunks, embedding_function=emb, persist_directory="./chroma_db")
vectordb.persist()
print("向量化完成！")
