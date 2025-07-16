import random
from src.dataset import packageChatbot
from src.dataset import packageUser	
from machineBasic import machineWrite

isChat = True

#The chatbot introduces itself and asks us any questions we may have:
machineWrite("BOT: " + random.choice(packageChatbot["saludos"]) + random.choice(packageChatbot["presentaciones"])+ random.choice(packageChatbot["preguntas"]))

while isChat:
	answer = input("YOU: /> ").lower()
	for search in packageUser["saludoSimple"]:
		if search in answer:
			machineWrite("BOT: " + random.choice(packageChatbot["saludosUser"]))
	for search in packageUser["preguntasSimples"]:
		if search in answer:
			machineWrite("BOT: " + random.choice(packageChatbot["contar"]))
			op = input("YOU /> ").lower()
			if "si" or "tambien" or "claro" in op:
				machineWrite("BOT: " + random.choice(packageChatbot["rtaFina2"]))
	for search in packageUser["bienestar"]:
		if search in answer:
			machineWrite("BOT: " + random.choice(packageChatbot["rtaFina"]))
	for search in packageUser["finaliza"]:
		if search in answer:
			machineWrite("BOT: " + random.choice(packageChatbot["despedida"]))
			isChat = False
