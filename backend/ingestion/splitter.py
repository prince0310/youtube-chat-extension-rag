# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from ingestion import transcript
# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# chunks = splitter.create_documents([transcript])

from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(transcript: str, video_id: str):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.create_documents([transcript])

    for i, chunk in enumerate(chunks):
        chunk.metadata.update({
            "video_id": video_id,
            "chunk_id": i
        })

    return chunks