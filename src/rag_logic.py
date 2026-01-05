import os
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from langchain_community.vectorstores import Chroma  
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import RetrievalQA # Fix: Added 'A'

import os
from dotenv import load_dotenv
load_dotenv()

# Now use the variable instead of the hardcoded string
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# 2. Load Vector Store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = Chroma(persist_directory="../vector_store/", embedding_function=embeddings)

# Initialize the endpoint using Llama 3.1 
# This model has very high availability on the free API
endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", 
    task="text-generation", 
    temperature=0.1,
    max_new_tokens=512,
    huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
)

llm = ChatHuggingFace(llm=endpoint)
# 4. Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are a financial analyst for CrediTrust. Answer the question using ONLY the context.
Context: {context}
Question: {question}
Answer:""")

# 5. Build RAG Chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_db.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

def ask_creditrust(query):
    result = rag_chain.invoke({"query": query})
    return result["result"], result["source_documents"]

if __name__ == "__main__":
    ans, docs = ask_creditrust("What are the main issues with credit cards?")
    print(f"\nAI ANSWER:\n{ans}")