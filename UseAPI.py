import openai
import json
from decouple import config

API_KEY = config("OPENAI_KEY")

openai.api_key = API_KEY

models = openai.Model.list()

response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = "Hello",
    temperature = 0.95,
    max_tokens = 10,
)

print(response)