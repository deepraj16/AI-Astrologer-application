# 🌌 AI Astrologer Application  

An interactive Flask-based web application that provides **personalized astrology readings** and **AI-powered chat**.  
It combines **astrological calculations** with **LLM responses** (powered by Mistral AI) to deliver comprehensive insights.  

---
<img width="1736" height="891" alt="image" src="https://github.com/user-attachments/assets/ea61faf6-7fd3-4809-b1c3-2f5dfa0eadc5" />

<img width="1734" height="911" alt="image" src="https://github.com/user-attachments/assets/e2f1cfdf-e2d8-4c51-95e9-4b0052ea97d4" />

<img width="1436" height="927" alt="image" src="https://github.com/user-attachments/assets/4e07b709-bdd1-4516-b23d-5caa617e5767" />


## ✨ Features
- Generate an astrology reading based on:
  - Name
  - Birth date
  - Birth time
  - Birth place  
- Zodiac sign, element, and quality calculation.  
- Interactive chat with an AI astrologer (session-aware).  
- Conversation history for each user session.  
- Clear session and start fresh anytime.  

---

## ⚙️ Tech Stack
- **Backend**: Flask (Python)  
- **AI/LLM**: [LangChain MistralAI](https://python.langchain.com/docs/integrations/chat/mistralai)  
- **Astrology Engine**: Custom `AstrologyEngine` for zodiac calculations  
- **Frontend**: HTML + JavaScript (AJAX requests)  

---

## 📂 Project Structure
AI-Astrologer-application/
│── app.py # Main Flask application
│── astrology_engine.py # Custom astrology utility engine
│── templates/
│ └── index.html # Frontend UI
│── static/
│ └── style.css # Stylesheet
│── requirements.txt # Python dependencies
│── README.md # Project documentation  


---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/deepraj16/AI-Astrologer-application.git
cd AI-Astrologer-application  
```
2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Set environment variables

Add your MistralAI API Key to the environment:

export MISTRAL_API_KEY="your_api_key_here"     # Linux/Mac
set MISTRAL_API_KEY=your_api_key_here          # Windows

5. Run the application
flask run


By default, the app runs at: http://127.0.0.1:5000

Clears the current user’s session and conversation.

📸 Screenshots

(Add screenshots of your UI here once available)

### 🌠 Future Improvements

Add natal chart visualization.

Improve birthplace to latitude/longitude conversion (via geocoding).

Support multiple AI models (OpenAI, Groq, Anthropic, etc.).
