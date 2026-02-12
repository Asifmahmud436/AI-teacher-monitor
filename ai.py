from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import json
from .constants import Prompt

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def summarizer(pdf_file):
    file = client.files.create(
        file=open(pdf_file, "rb"),
        purpose="user_data"
    )
    prompt = Prompt

    response = client.responses.create(
        model="gpt-5.2-pro",
        reasoning={"effort": "high"},
        response_format={"type": "json_object"},
        input=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "file_id": file.id,
                    }
                ]
            }
        ]
    )

    return json.loads(response.output_text)


# file = client.files.create(
#     file=open("2d38b3fe-5539-4edf-be66-aa4f235cba3d.pdf", "rb"),
#     purpose="user_data"
# )

# prompt = Prompt 

# response = client.responses.create(
#         model="gpt-5.2-pro",
#         reasoning={"effort": "high"},
#         input=[
#             {
#                 "role": "system",
#                 "content": prompt
#             },
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "input_file",
#                         "file_id": file.id,
#                     }
#                 ]
#             }
#         ]
#     )
# try:
#     # প্রথমে নিশ্চিত হয়ে নিচ্ছি এটা ভ্যালিড JSON কি না
#     analysis_data = json.loads(response.output_text)
    
#     # এবার ফাইলটি সেভ করছি
#     output_filename = "teacher_analysis_report.txt"
#     with open(output_filename, "w", encoding="utf-8") as f:
#         # indent=4 দিলে ফাইলটি দেখতে সুন্দর এবং পড়ার যোগ্য হবে
#         json.dump(analysis_data, f, indent=4, ensure_ascii=False)
        
#     print(f"Analysis successfully saved to: {output_filename}")

# except Exception as e:
#     print(f"Error saving file: {e}")

