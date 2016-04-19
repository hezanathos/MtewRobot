# -*-coding:iso-8859-15-*
import re


def retrieve_message_by_key(adress, key):
   	print(adress)
	try:
	        fichierPropertiesFR = open(adress, "r")
	        contenu = fichierPropertiesFR.read()
	        properties = contenu.split("\n")
       		regexStringName = r"^[ ]*" + key + "[ ]*$"

	        for properti in properties:
	            valeur = properti.split("=")
	            if re.search(regexStringName, valeur[0]):
	                print(valeur[1].strip())
	                return valeur[1].strip()
        	raise AssertionError("No such key in properties file")
        except IOError:
        	print("No such file at given address")
