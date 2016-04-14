#-*-coding:Utf-8-*

def k_w(element):
	num = element[-1]
	num = int(num)
	num += 1
	res = "Q"+str(num)+"-question"
	return res

def k_p(element):
	num = element[-1]
	num = int(num)
	num += 1
	res = "answerRadio"+str(num)+"1"
	return res

def print_exp(exp):
	print(exp)