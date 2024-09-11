import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

EDEN_API_KEY = os.getenv("EDEN_API_KEY")


class Bot:
    def __init__(self) -> None:
        self._history = []

    def chat(self, prompt):
        headers = {"Authorization": f"Bearer {EDEN_API_KEY}"}

        url = "https://api.edenai.run/v2/text/chat"
        payload = {
            "providers": "openai/gpt-4o-mini",
            "text": prompt,
            "chatbot_global_action":
             """You will have several different personalities 
             1: a summarizer in simpler language. 
             2: an expert in resume building. 
             3: an expert in resume summarizing. 
             4: a culinary expert that based on what ingredients you put in can give suggestions on recipes. 
             5: one data analyst which can take data and generate a plot.

             Change your name after what personality you have and always start the message with your name and then the text

            """,
            "previous_history": self._history,
            "temperature": 0.5,
            "max_tokens": 150,
        }

        response = requests.post(url, json=payload, headers=headers)
        answer = json.loads(response.text)["openai/gpt-4o-mini"]["generated_text"]

        self._history.append({"role": "user", "message": prompt})
        self._history.append({"role": "assistant", "message": answer})

        return answer


bot = Bot()
bot.chat("Tell me a joke ")