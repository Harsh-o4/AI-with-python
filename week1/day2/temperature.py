import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API")
if not my_api_key:
    raise ValueError("NO API KEY FOUND")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

system_role = {
    "role" : "system",
    "content" : "You are a brand manager"
}

role = "user"
prompt = "Suggest me a name for my new clothing brand. The name should be of 1 word only. Suggest me 5 names to choose from"

message = {
    "role": role,
    "content" : prompt
}

messages = [system_role,message]

#temperature generally ranges from 0(basic) to 2(creative)
response = client.chat.completions.create(model=model,messages=messages,temperature=2)
print(response.choices[0].message.content)