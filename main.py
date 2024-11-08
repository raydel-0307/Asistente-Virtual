from functions import *
from utils import *

def query(q):
	if q:
		msg = proccess_data(q)

		data = clean_json(msg)

		if data["function"]=="weather":
			return proccess_data(q,type="Weather",args=get_weather(data["args"]))
		else:
			return "No se pudo procesar su información"
	else:
		return "Message: Error, ingrese su pregunta"

def main():
	print("IA: Hola, en que puedo ayudarte hoy:\n")

	while True:
		prompt = input("You: ")

		print("\nIA:",query(prompt))

		print("\nIA: En que más puedo ayudarte?\n")

if __name__=="__main__":
	main()