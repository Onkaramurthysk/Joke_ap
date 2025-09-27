
from sqlalchemy.orm import Session
from models import Joke
from schemas import JokeCreate

def create_joke(db: Session, joke: JokeCreate):
    db_joke = Joke(**joke.dict())
    db.add(db_joke)
    db.commit()
    db.refresh(db_joke)
    return db_joke
