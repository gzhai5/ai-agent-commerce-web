from openai import OpenAI
from app.config import settings


class OpenAIUtils:
    def __init__(self):
        self.openai_client = OpenAI(api_key=settings.openai_api_key)

    def openai_model_analyze_image(self, text: str, model='gpt-4.1-mini', image_url='') -> str:
        response = self.openai_client.responses.create(
            model=model,
            input=[
                {
                    "role": "user",
                    "content": [
                        { "type": "input_text", "text": f"{text}" },
                        {
                            "type": "input_image",
                            "image_url": f"{image_url}"
                        }
                    ]
                }
            ]
        )
        return response.output_text
        
openai_utils = OpenAIUtils()