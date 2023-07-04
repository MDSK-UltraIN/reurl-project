from fastapi import FastAPI
from pydantic import BaseModel
import secrets

app = FastAPI()

# start uvicorn server:
# uvicorn main:app --reload


class URL(BaseModel):
    url: str


def generate_short_url():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    short_url = "".join(secrets.choice(alphabet) for _ in range(6))
    return short_url


@app.get("/")
def read_main():
    return {"Hello": "World"}


@app.post("/shorten")
def shorten_url(url: URL):
    # return url
    short_url = generate_short_url()
    return {"original_url": url.url, "short_url": short_url}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
