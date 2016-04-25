#-*-coding:Utf-8-*

def k_bon_id(element):
	num = element[-1]
	num = int(num)
	num += 1
	res = "Q"+str(num)+"-question"
	return res

def k_coche_bonne_reponse(element):
	num = element[-1]
	num = int(num)
	num += 1
	res = "answerRadio"+str(num)+"1"
	return res

def k_index(element):
	num = element[-1]
	num = int(num)
	return num

def level(num):
	if num =="0":
		return "Techadmin"
	elif num == "1":
		return "Projectadmin"
	else:
		return "none"

def print_exp(exp):
	print(exp)