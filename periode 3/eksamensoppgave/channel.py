from pydantic import BaseModel, Field


class Channel(BaseModel):
    country: str = Field(alias="Country")
    subscribers: int
    video_views: int = Field(alias="video views")
