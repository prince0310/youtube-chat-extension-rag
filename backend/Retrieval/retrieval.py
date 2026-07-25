# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_qdrant import QdrantVectorStore
# # from qdrant_client import QdrantClient

# # # -----------------------------
# # # Embedding Model
# # # -----------------------------
# # embeddings = HuggingFaceEmbeddings(
# #     model_name="BAAI/bge-small-en-v1.5"
# # )

# # # -----------------------------
# # # Qdrant Client
# # # -----------------------------
# # client = QdrantClient(
# #     url="http://localhost:6333",
# # )

# # # -----------------------------
# # # Vector Store
# # # -----------------------------
# # vector_store = QdrantVectorStore(
# #     client=client,
# #     collection_name="youtube-chat",
# #     embedding=embeddings,
# # )

# # # -----------------------------
# # # Retriever
# # # -----------------------------
# # retriever = vector_store.as_retriever(
# #     search_type="mmr",
# #     search_kwargs={
# #         "k": 4,
# #         "fetch_k": 20
# #     }
# # )
# # # -----------------------------
# # # Test Query
# # # -----------------------------
# # query = "What is DeepMind?"

# # docs = retriever.invoke(query)

# # print(f"\nQuery: {query}\n")
# # print("=" * 80)

# # for i, doc in enumerate(docs, start=1):
# #     print(f"\nChunk {i}")
# #     print("-" * 80)
# #     print(doc.page_content)


# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_qdrant import QdrantVectorStore
# from qdrant_client import QdrantClient


# embeddings = HuggingFaceEmbeddings(
#     model_name="BAAI/bge-small-en-v1.5"
# )

# client = QdrantClient(
#     url="http://localhost:6333",
# )

# vector_store = QdrantVectorStore(
#     client=client,
#     collection_name="youtube-chat",
#     embedding=embeddings,
# )

# retriever = vector_store.as_retriever(
#     search_type="mmr",
#     search_kwargs={
#         "k": 4,
#         "fetch_k": 20,
#     },
# )


# def retrieve(query: str):
#     return retriever.invoke(query)

# # if __name__ == "__main__":
# #     docs = retrieve("What is DeepMind?")

# #     for i, doc in enumerate(docs, 1):
# #         print(f"\nChunk {i}")
# #         print(doc.page_content)
from services.qdrant_manager import QdrantManager

qdrant = QdrantManager()


def get_retriever(video_id: str):
    return qdrant.get_retriever(video_id)