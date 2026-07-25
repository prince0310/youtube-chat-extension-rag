from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    Filter,
    FieldCondition,
    MatchValue,
)

COLLECTION_NAME = "youtube-chat"


class QdrantManager:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )

        self.client = QdrantClient(
            url="http://localhost:6333",
            timeout=60,
        )

    def create_collection(self):

        collections = {
            c.name
            for c in self.client.get_collections().collections
        }

        if COLLECTION_NAME in collections:
            return

        dimension = len(
            self.embeddings.embed_query("hello")
        )

        self.client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=dimension,
                distance=Distance.COSINE,
            ),
        )

    def get_vector_store(self):

        self.create_collection()

        return QdrantVectorStore(
            client=self.client,
            collection_name=COLLECTION_NAME,
            embedding=self.embeddings,
        )

    def get_retriever(self, video_id: str):

        vector_store = self.get_vector_store()

        return vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 8,
                "fetch_k": 20,
                "filter": Filter(
                    must=[
                        FieldCondition(
                            key="metadata.video_id",
                            match=MatchValue(value=video_id),
                        )
                    ]
                ),
            },
        )

    def is_video_indexed(self, video_id: str):

        self.create_collection()

        points, _ = self.client.scroll(
            collection_name=COLLECTION_NAME,
            scroll_filter=Filter(
                must=[
                    FieldCondition(
                        key="metadata.video_id",
                        match=MatchValue(value=video_id),
                    )
                ]
            ),
            limit=1,
        )

        return len(points) > 0