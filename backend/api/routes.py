from fastapi import APIRouter, HTTPException

from api.schemas import (
    IndexRequest,
    IndexResponse,
    ChatRequest,
    ChatResponse,
)

from services.rag_service import RAGService

router = APIRouter()


@router.post(
    "/index",
    response_model=IndexResponse,
)
def index_video(request: IndexRequest):

    try:
        result = RAGService.index(
            request.video_id
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    try:
        result = RAGService.chat(
            request.video_id,
            request.question,
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )