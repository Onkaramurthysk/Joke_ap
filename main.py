
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import requests

from database import SessionLocal, engine, Base
import models, crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/fetch-jokes/")
def fetch_jokes(db: Session = Depends(get_db)):
    jokes_url = "https://v2.jokeapi.dev/joke/Any?amount=10"  # JokeAPI supports max 10 per request
    total_fetched = 0

    while total_fetched < 100:
        response = requests.get(jokes_url)
        data = response.json()

        if "jokes" in data:
            for j in data["jokes"]:
                joke_data = {
                    "category": j["category"],
                    "type": j["type"],
                    "joke": j["joke"] if j["type"] == "single" else None,
                    "setup": j["setup"] if j["type"] == "twopart" else None,
                    "delivery": j["delivery"] if j["type"] == "twopart" else None,
                    "nsfw": j["flags"]["nsfw"],
                    "political": j["flags"]["political"],
                    "sexist": j["flags"]["sexist"],
                    "safe": j["safe"],
                    "lang": j["lang"]
                }
                crud.create_joke(db, schemas.JokeCreate(**joke_data))
                total_fetched += 1
                if total_fetched >= 100:
                    break

    return {"message": f"Fetched and stored {total_fetched} jokes successfully."}
