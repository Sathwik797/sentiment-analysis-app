# 📊 Sentiment Analysis API  

A RESTful API built with **Flask**, **NLTK**, and **Hugging Face Transformers** for performing **sentiment analysis** on text data.  
This project demonstrates **NLP preprocessing**, **transformer-based models**, and **cloud deployment**.  

---

## 🚀 Features  
- REST API using **Flask**  
- Text **preprocessing with NLTK** (stopword removal, tokenization, punctuation cleanup)  
- Sentiment classification using **Hugging Face pretrained transformer**  
- Returns both **original** and **cleaned text** with prediction results  
- Ready for **cloud deployment** (Heroku / Render / Railway / AWS)  

---

## 📂 Project Structure  
sentiment-analysis-api/
│── app.py # Flask app (main API code)
│── requirements.txt # Dependencies
│── Procfile # (Heroku deployment)
│── runtime.txt # Python version (for Heroku)
│── README.md # Documentation

---

## ⚙️ Installation  

1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/sentiment-analysis-api.git
cd sentiment-analysis-api

2️⃣ Create a virtual environment & activate it
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running Locally
python app.py
API will start at:
👉 http://127.0.0.1:5000/

📡 API Endpoints
🔹 Home (Check API status)

GET /
Response: { "message": "✅ Sentiment Analysis API with NLTK + Hugging Face is running!" }

🔹 Predict Sentiment

POST /predict
Request Body (JSON):
{
  "text": "I love this project!"
}
Response:
{
  "original_text": "I love this project!",
  "cleaned_text": "love project",
  "label": "POSITIVE",
  "score": 0.9994
}


🛠️ Tech Stack
 Python
 Flask
 NLTK (text preprocessing)
 Hugging Face Transformers (sentiment analysis)

✨ Future Improvements
 Add support for multiple languages
 Deploy with Docker + AWS/GCP
 Build a frontend UI for easy interaction

👨‍💻 Author
Sathwik Reddy Obilipapannagari

