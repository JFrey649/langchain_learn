from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

emb = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="./chroma_db", embedding_function=emb)
retriever = vectordb.as_retriever(search_kwargs={"k": 2})

docs = retriever.get_relevant_documents("如何计算PIV？")
print([d.page_content for d in docs])
