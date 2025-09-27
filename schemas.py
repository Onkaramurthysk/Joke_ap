
from pydantic import BaseModel

class JokeCreate(BaseModel):
    category: str
    type: str
    joke: str | None = None
    setup: str | None = None
    delivery: str | None = None
    nsfw: bool
    political: bool
    sexist: bool
    safe: bool
    lang: str

    class Config:
        orm_mode = True
