# 📊 Sentiment Analysis API

A Flask REST API for sentiment analysis using NLTK preprocessing and a pretrained Hugging Face Transformer model.

## ✨ Features

- REST API built with Flask
- Text preprocessing with NLTK
- Transformer-based sentiment classification
- Returns original text, cleaned text, predicted label, and confidence score
- Simple API structure suitable for cloud deployment

## 🛠️ Tech Stack

- Python
- Flask
- NLTK
- Hugging Face Transformers

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md
```

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/Sathwik797/sentiment-analysis-app.git
cd sentiment-analysis-app
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\\Scripts\\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
python app.py
```

The API runs locally on `http://127.0.0.1:5000/`.

## 📡 API

### Health Check

`GET /`

Returns the API status.

### Predict Sentiment

`POST /predict`

Request:

```json
{
  "text": "I love this project!"
}
```

Example response:

```json
{
  "original_text": "I love this project!",
  "cleaned_text": "love project",
  "label": "POSITIVE",
  "score": 0.9994
}
```

## 🔮 Future Improvements

- Multilingual sentiment analysis
- Containerized deployment
- Frontend interface for interactive predictions

## 👨‍💻 Author

**Sathwik Reddy**

GitHub: https://github.com/Sathwik797
