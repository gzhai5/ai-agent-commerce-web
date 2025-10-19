from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime
from typing import Optional


class Feedback(BaseModel):
    feedbackGiven: bool = False
    positiveFeedback: str = ""
    negativeFeedback: str = ""


class MessageModel(BaseModel):
    id: str  = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    sessionId: str = Field(required=True, alias="sessionId")
    sender: str = Field(default="user", alias="sender")
    content: str = Field(default="", alias="content")
    action: dict | None = Field(default=None, alias="action")
    timestamp: datetime = Field(default_factory=datetime.utcnow, alias="timestamp")
    feedback: Feedback | None = Field(default=None, alias="feedback")
    queryType: Optional[str] = Field(default=None, alias="queryType")
    responseTime: Optional[float] = Field(default=None, alias="responseTime") # in milliseconds
