import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API")
if not my_api_key:
    raise ValueError("No Api Key found")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

class Ticket(BaseModel):
    name:str
    email:str
    phone:int
    issue:str
schema = Ticket.model_json_schema()

responseFormat = {
    "type":"json_object"
}

systemPrompt = f"""
Extract personal information from the ticket strictly based on this schema {schema} in json format
"""

system_message = {
    "role":"system",
    "content":systemPrompt
}

role = "user"
text = "Helo! my name is Harsh. I bought an appliance from you store which appears to be defective. Contact me on harshsingh3776@ gmail.com or my phone number 9876543210. I live in India and I am a computer science student"
prompt = f"""
This is a ticket filed by a customer. Extract personal information from this {text}
"""

message = {
    "role":role,
    "content":prompt
}

messages = [system_message,message]

reponse = client.chat.completions.create(model=model,messages=messages)
ans = reponse.choices[0].message.content    
print(ans)

#using JSON output
import json 
raw_json = ans
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)