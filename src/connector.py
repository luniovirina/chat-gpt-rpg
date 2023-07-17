import openai
from config import settings

openai.organization = settings.organization
openai.api_key = settings.OPENAI_API_KEY


class openAiConnector:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def connect(self):
        return openai.ChatCompletion.create(
            model=settings.model,
            messages=[
                {"role": self.role, "content": self.content},
            ],
        )
