# from ingestion.embedding_generation import index_video
# from chains.rag_chain import get_rag_chain


# class RAGService:

#     @staticmethod
#     def index(video_id: str):
#         return index_video(video_id)

#     @staticmethod
#     def chat(video_id: str, question: str):

#         rag_chain = get_rag_chain(video_id)

#         response = rag_chain.invoke(
#             {
#                 "input": question
#             }
#         )

#         return {
#             "answer": response["answer"]
#         }

from ingestion.embedding_generation import index_video
from chains.rag_chain import get_rag_chain
from Retrieval.retrieval import get_retriever


class RAGService:

    @staticmethod
    def index(video_id: str):
        return index_video(video_id)

    @staticmethod
    def chat(video_id: str, question: str):

        retriever = get_retriever(video_id)

        docs = retriever.invoke(question)

        print("\n========== RETRIEVED DOCUMENTS ==========")
        print(f"Retrieved: {len(docs)} documents")

        for i, doc in enumerate(docs, 1):
            print(f"\n----- Document {i} -----")
            print(doc.metadata)
            print(doc.page_content[:300])

        rag_chain = get_rag_chain(video_id)

        response = rag_chain.invoke(
            {
                "input": question
            }
        )

        return {
            "answer": response["answer"]
        }