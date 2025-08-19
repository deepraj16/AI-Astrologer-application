from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import os
from langchain_mistralai.chat_models import ChatMistralAI
from astrology_engine import AstrologyEngine

app = Flask(__name__)
app.secret_key = "astrology_secret"

def setup_llm():
    return ChatMistralAI(api_key="lHcwga2vJ6yyjV470WdMIFn5hRgtMbcc")

llm = setup_llm()
astro_engine = AstrologyEngine()

conversations = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_reading", methods=["POST"])
def generate_reading():
    try:
        data = request.get_json()
        name = data.get("name", "").strip()
        birth_date = data.get("birth_date", "").strip()
        birth_time = data.get("birth_time", "").strip()
        birth_place = data.get("birth_place", "").strip()

        if not all([name, birth_date, birth_place]):
            return jsonify({"success": False, "error": "Name, date, and place are required."})

        try:
            birth_datetime = datetime.strptime(birth_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"success": False, "error": "Date must be in YYYY-MM-DD format."})

        zodiac_info = astro_engine.get_zodiac_sign(birth_datetime.month, birth_datetime.day)

        session["user_data"] = {
            "name": name,
            "birth_date": birth_date,
            "birth_time": birth_time,
            "birth_place": birth_place,
            "zodiac_sign": zodiac_info["sign"],
            "element": zodiac_info["element"],
            "quality": zodiac_info["quality"],
        }

        if "session_id" not in session:
            session["session_id"] = f"session_{datetime.now().timestamp()}"
        conversations[session["session_id"]] = []

        reading = astro_engine.generate_comprehensive_reading(
            name, zodiac_info, birth_place, birth_time, llm
        )

        return jsonify({
            "success": True,
            "reading": reading,
            "zodiac_info": zodiac_info,
            "user_data": session["user_data"]
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"success": False, "error": "Please enter a message"})

        session_id = session.get("session_id")
        user_data = session.get("user_data")

        if not session_id or not user_data:
            return jsonify({"success": False, "error": "Please generate your reading first."})
        history = conversations.get(session_id, [])
        prompt = f"""You are an astrologer. 
        User: {user_data['name']}
        Zodiac: {user_data['zodiac_sign']} ({user_data['element']}, {user_data['quality']})
        Birth Place: {user_data['birth_place']}
        Birth Time: {user_data['birth_time']}

        Conversation so far:
        {chr(10).join(history)}

        User Question: {user_message}
        Astrologer:"""
     
        response = llm.invoke(prompt).content
   
        history.append(f"User: {user_message}")
        history.append(f"Astrologer: {response}")
        conversations[session_id] = history

        return jsonify({"success": True, "response": response})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/clear_session", methods=["POST"])
def clear_session():
    sid = session.get("session_id")
    if sid in conversations:
        del conversations[sid]
    session.clear()
    return jsonify({"success": True, "message": "Session cleared."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)