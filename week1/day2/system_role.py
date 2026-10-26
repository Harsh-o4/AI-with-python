import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API")
if not my_api_key:
    raise ValueError("No Api Key found")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

# both system roles will produce different outputs

# system_role= {
#     "role":"system",
#     "content":"You are a stock broker"
# }

system_role= {
    "role":"system",
    "content":"You are a software engineer"
}

role = "user"
prompt = "what one advice would you give to freshers that are just starting out?"

message = {
    "role":role,
    "content":prompt
}

messages = [system_role,message]

reponse = client.chat.completions.create(model=model,messages=messages)
print(reponse.choices[0].message.content)

