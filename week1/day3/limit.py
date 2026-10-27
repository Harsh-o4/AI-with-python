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
}

role = "user"
prompt1 = "Hi"
prompt2 = "Explain array in detail"
prompt3 = "write a 500 word essay on Constitution"

prompts = [prompt1,prompt2,prompt3]

for prompt in prompts:
    message = {
        "role" : role,
        "content" : prompt
    }

    messages = [message]
    response = client.chat.completions.create(model=model,messages=messages, max_tokens=50)

    usage = response.usage
    print(f"Prompt: {prompt}--->IP token: {usage.prompt_tokens} OP token: {usage.completion_tokens} total token: {usage.total_tokens} Finish reason: {response.choices[0].finish_reason}")
