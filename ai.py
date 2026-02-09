from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

file = client.files.create(
    file=open("response.pdf", "rb"),
    purpose="user_data"
)

response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": "Summarize the pdf",
                },
            ]
        }
    ]
)

print(response.output_text)