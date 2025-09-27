# Joke API Project 

This project is a **FastAPI-based application** that fetches jokes from the [JokeAPI](https://sv443.net/jokeapi/v2/), processes them, and stores them in a local SQLite database.

---

## 🚀 Features
- Fetches jokes from JokeAPI (batch of 10 per request).
- Stores **at least 100 jokes** in the database.
- Extracts and stores:
  - `category`
  - `type`
  - `joke` (for single type)
  - `setup` and `delivery` (for two-part jokes)
  - `flags.nsfw`, `flags.political`, `flags.sexist`
  - `safe`
  - `lang`
- Exposes an endpoint to trigger fetching and storing.

---

## 📂 Project Structure
joke_api_project/
│── main.py # FastAPI app entry point
│── models.py # SQLAlchemy models
│── database.py # DB connection setup
│── crud.py # CRUD operations
│── schemas.py # Pydantic schemas
│── requirements.txt # Dependencies
│── README.md # Documentation
