from openai import OpenAI
from os import getenv
from dotenv import load_dotenv

load_dotenv()

apikey = getenv("OPENAI_API_KEYY")
print("API Key:", apikey)
client = OpenAI(api_key=getenv("OPENAI_API_KEYY"))

def get_response_from_model(prompt):
	response = client.responses.create(
		model="gpt-4.1",
		input=prompt
		)
	return response.output_text
