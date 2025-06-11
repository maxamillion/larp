from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List

# Hardcoded data (replace with your actual data)
data: List[str] = [
    "This is a sample document about CrewAI.",
    "CrewAI is a framework for creating autonomous agents.",
    "The agents can work together to solve complex problems.",
    "Each agent has a specific role and goal.",
    "The agents can use tools to access information.",
]

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.create_documents(data)

# Create embeddings using HuggingFaceEmbeddings
hhf_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Generate embeddings for the chunks
embeddings = hhf_embeddings.embed_documents([chunk.page_content for chunk in chunks])

# Check for empty embeddings
if not embeddings:
    print("Error: No embeddings were generated.")
    exit()

# Store the embeddings in ChromaDB
vectordb = Chroma.from_documents(chunks, embedding=hhf_embeddings, persist_directory="chroma_db")
vectordb.persist()

print("Data ingestion complete.")