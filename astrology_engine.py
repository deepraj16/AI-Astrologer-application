from typing import Dict

class AstrologyEngine:
    """Minimal astrology engine with core functionality"""
    
    def __init__(self):
        self.signs = [
            {"sign": "Capricorn", "dates": (12, 22, 1, 19), "element": "Earth"},
            {"sign": "Aquarius", "dates": (1, 20, 2, 18), "element": "Air"},
            {"sign": "Pisces", "dates": (2, 19, 3, 20), "element": "Water"},
            {"sign": "Aries", "dates": (3, 21, 4, 19), "element": "Fire"},
            {"sign": "Taurus", "dates": (4, 20, 5, 20), "element": "Earth"},
            {"sign": "Gemini", "dates": (5, 21, 6, 20), "element": "Air"},
            {"sign": "Cancer", "dates": (6, 21, 7, 22), "element": "Water"},
            {"sign": "Leo", "dates": (7, 23, 8, 22), "element": "Fire"},
            {"sign": "Virgo", "dates": (8, 23, 9, 22), "element": "Earth"},
            {"sign": "Libra", "dates": (9, 23, 10, 22), "element": "Air"},
            {"sign": "Scorpio", "dates": (10, 23, 11, 21), "element": "Water"},
            {"sign": "Sagittarius", "dates": (11, 22, 12, 21), "element": "Fire"}
        ]
        
        self.traits = {
            "Aries": "Bold leader, energetic pioneer. Challenge: impatience.",
            "Taurus": "Reliable, practical stability. Challenge: stubbornness.",
            "Gemini": "Quick-witted communicator. Challenge: inconsistency.",
            "Cancer": "Nurturing intuitive protector. Challenge: moodiness.",
            "Leo": "Creative generous performer. Challenge: ego-driven.",
            "Virgo": "Detail-oriented helpful perfectionist. Challenge: overcritical.",
            "Libra": "Diplomatic harmony-seeker. Challenge: indecision.",
            "Scorpio": "Intense passionate transformer. Challenge: jealousy.",
            "Sagittarius": "Adventurous optimistic explorer. Challenge: tactlessness.",
            "Capricorn": "Disciplined ambitious achiever. Challenge: pessimism.",
            "Aquarius": "Independent humanitarian innovator. Challenge: detachment.",
            "Pisces": "Compassionate artistic dreamer. Challenge: escapism."
        }

    def get_zodiac_sign(self, month: int, day: int) -> Dict:
        """Returns zodiac sign, element, and quality for birth date"""
        for sign_data in self.signs:
            sm, sd, em, ed = sign_data["dates"]
            
            if sm > em: 
                if (month == sm and day >= sd) or (month == em and day <= ed):
                    return {
                        "sign": sign_data["sign"], 
                        "element": sign_data["element"],
                        "quality": "Cardinal" 
                    }
            else:
                if (month == sm and day >= sd) or (month == em and day <= ed) or (sm < month < em):
                    return {
                        "sign": sign_data["sign"], 
                        "element": sign_data["element"],
                        "quality": "Cardinal" 
                    }
        
        return {"sign": "Unknown", "element": "Unknown", "quality": "Unknown"}

    def generate_comprehensive_reading(self, name: str, zodiac_info: Dict, birth_place: str, birth_time: str, llm) -> str:
        """Generates comprehensive reading using LLM"""
        sign = zodiac_info["sign"]
        element = zodiac_info["element"]
        
        if sign == "Unknown":
            return f"Hello {name}, unable to determine your sign. Please check your birth date."
        
        # Create prompt for LLM
        prompt = f"""Create a warm, personalized 40-word astrological reading for {name}.
        
        Details: {sign} sign, {element} element, born in {birth_place}
        Traits: {self.traits.get(sign, 'Unique individual')}
        
        Include: personality insight, life guidance, current advice. Keep it positive and empowering."""
        
        try:
            response = llm.invoke(prompt).content
            return response
        except Exception as e:
            traits = self.traits[sign]
            return f"{name}, as a {sign} ({element}), {traits} Born in {birth_place}, your {element.lower()} nature guides you. Current focus: embrace strengths while managing challenges. Trust your instincts! ✨"