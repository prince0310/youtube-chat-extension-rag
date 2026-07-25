from pydantic import BaseModel


class IndexRequest(BaseModel):
    video_id: str


class IndexResponse(BaseModel):
    status: str
    message: str


class ChatRequest(BaseModel):
    video_id: str
    question: str


class ChatResponse(BaseModel):
    answer: str