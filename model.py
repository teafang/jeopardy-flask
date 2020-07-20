import requests
import random

API_endpoint = "https://jservice.io/api/clues"
API_query = "value=1000"
API_URL = API_endpoint + "?" + API_query
r = requests.get(API_URL)
data = r.json()

def random_question():
  return data[random.randint(0, len(data))]