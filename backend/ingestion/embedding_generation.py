from ingestion.ingestion import get_transcript
from ingestion.splitter import create_chunks

from services.qdrant_manager import QdrantManager


qdrant = QdrantManager()


def index_video(video_id: str):

    if qdrant.is_video_indexed(video_id):

        return {
            "status": "already_indexed",
            "message": "Video already indexed."
        }

    transcript = get_transcript(video_id)

    if transcript is None:
        raise Exception("Transcript not found.")

    chunks = create_chunks(
        transcript,
        video_id,
    )

    vector_store = qdrant.get_vector_store()

    vector_store.add_documents(chunks)

    return {
        "status": "indexed",
        "message": "Video indexed successfully."
    }