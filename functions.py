import requests
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoderMonitor
from requests_toolbelt import MultipartEncoder
from functools import partial
import uuid
import requests_toolbelt as rt
import mimetypes
import json
import re
import os
from fake_useragent import UserAgent
from utils import *
from huggingface_hub import InferenceClient

def get_weather(city):
	api_key = get_info("OpenWeatherMap_ApiKey")
	url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
	response = json.loads(requests.get(url).text)
	return response

def proccess_data(texto,type="Default",args=None):
	
	if type=="Default":
		with open("data/instruct.txt", 'r', encoding='utf-8') as file:
			text = file.read()
		text+=f"\n\nPrompt: {texto}"
		text+="\n\nMandame solo el json"

	elif type=="Weather":
		text = "Según estos datos\n\n"
		text+= str(args)
		text+= f"\n{texto}"
		text+= "\nMandame solo la respuesta"

	return query(text)

def query(text):
	client = InferenceClient(api_key=get_info("HuggingFace_ApiKey"))
	messages = [
		{
			"role":"user",
			"content":text
		}
	]

	stream = client.chat.completions.create(
		model=get_info("model_name"),
		messages=messages,
		max_tokens=get_info("max_tokens"),
		stream=True
	)

	response = ""
	for chunk in stream:
		response+=chunk.choices[0].delta.content
	
	return response
