from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)
from langchain_classic.chains.retrieval import (
    create_retrieval_chain,
)

from Retrieval.retrieval import get_retriever
from chains.prompts import rag_prompt


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
)


document_chain = create_stuff_documents_chain(
    llm,
    rag_prompt,
)


def get_rag_chain(video_id: str):
    """
    Returns a retrieval chain scoped to a single YouTube video.
    """

    retriever = get_retriever(video_id)

    return create_retrieval_chain(
        retriever,
        document_chain,
    )