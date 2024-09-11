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
            "chatbot_global_action": """AnalystGPT - send in some data and it will give some KPIs, or even make graphs based on your data
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