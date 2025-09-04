from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import os

# Download NLTK resources (only first run)
nltk.download("punkt")
nltk.download("stopwords")

# Flask app
app = Flask(__name__)

# Load pre-trained sentiment analysis model (Hugging Face)
sentiment_pipeline = pipeline("sentiment-analysis")

# Preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords & punctuation
    tokens = [
        word for word in tokens
        if word not in stopwords.words("english") and word not in string.punctuation
    ]
    return " ".join(tokens)

@app.route("/")
def home():
    return {"message": "✅ Sentiment Analysis API with NLTK + Hugging Face is running!"}

# ---------- Batch + Single UI ----------
@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/predict-ui", methods=["POST"])
def predict_ui():
    try:
        text = request.form.get("text", "")
        if not text.strip():
            return render_template("index.html", results=None)

        # Split into sentences (by newlines or periods)
        sentences = [s.strip() for s in text.replace("\n", ". ").split(".") if s.strip()]

        results = []
        for sentence in sentences:
            clean_text = preprocess_text(sentence)
            pred = sentiment_pipeline(clean_text)[0]

            label = pred["label"].lower()
            score = float(pred["score"])
            if score < 0.7:  # low confidence → neutral
                label = "neutral"

            results.append({
                "original": sentence,
                "cleaned": clean_text,
                "label": label,
                "score": round(score, 4)
            })

        return render_template("index.html", results=results)

    except Exception as e:
        return render_template("index.html", error=str(e))

# ---------- JSON API (batch supported too) ----------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        sentences = [s.strip() for s in text.replace("\n", ". ").split(".") if s.strip()]

        results = []
        for sentence in sentences:
            clean_text = preprocess_text(sentence)
            pred = sentiment_pipeline(clean_text)[0]

            label = pred["label"].lower()
            score = float(pred["score"])
            if score < 0.7:
                label = "neutral"

            results.append({
                "original_text": sentence,
                "cleaned_text": clean_text,
                "label": label,
                "score": score
            })

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
