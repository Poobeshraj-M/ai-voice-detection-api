from pydantic import BaseModel
from typing import List

class DetectVoiceRequest(BaseModel):
    audio_url: str

class DetectVoiceResponse(BaseModel):
    status: str
    message: str
