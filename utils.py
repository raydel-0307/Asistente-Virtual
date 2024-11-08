import os
import json
import re

def clean_json(text):
	try:return json.loads(re.search(r'\{.*?\}', text).group(0))
	except:return json.loads(text)

def get_info(name):

	with open("data/config.json", 'r', encoding='utf-8') as file:
		data = json.loads(file.read())

	return data[name]