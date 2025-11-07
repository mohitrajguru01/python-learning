from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from textblob import TextBlob
import logging

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple sentiment analysis API using TextBlob",
    version="1.0.0"
)

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Request body model
class TextRequest(BaseModel):
    text: str


@app.get("/")
def root():
    """
    Root endpoint to verify API is running.
    """
    logger.info("Health check endpoint called.")
    return {"message": "Sentiment API is running successfully 🚀"}


@app.post("/predict")
def analyze_sentiment(request: TextRequest):
    """
    Predict sentiment polarity of a given text.
    """
    text = request.text.strip()

    if not text:
        logger.error("Empty text received.")
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 3)

    sentiment = (
        "positive" if polarity > 0 else
        "negative" if polarity < 0 else
        "neutral"
    )

    logger.info(f"Text: {text} | Polarity: {polarity} | Sentiment: {sentiment}")
    return {
        "text": text,
        "polarity": polarity,
        "sentiment": sentiment
    }


# For local dev mode
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
