from Backend import *
import re

Settings = {
	"minlength" : 3,
	"maxlength" : 4,
	"legal" : {
		"Syllable Structures" : ["cv"],
		"C" : list("bcdfghjklmnpqrstvwxyz"),
		"V" : list("aeiou")
	}
}


def main():
	options = {
		"Settings" : "settings()",
		"Start" : "Start()"
	}
	while True:
		x = 0
		for i in options:
			print(f"{x} - {i}")
			x +=1
		print("X - Exit")
		choice = input("Choose option: ")
		if choice.lower() == "x":
			break
		else:
			eval(options[list(options.keys())[int(choice)]])

def Start():
	a = input("Insert English phrase to translate... \n\n")

	key = {}
	for i in a.split(" "):
		i = re.sub("[^A-z]", "", i)
		key[i] = WordGen.WordGen(WordGen.SyllableGen(Settings["legal"]), random.randint(Settings["minlength"], Settings["maxlength"]))
	for x in list(key.keys()):
		a = a.replace(x,key[x])
	print("Translation: ")
	print(a)
	print("Vocabulary:")
	print(key)

def settings():
	while True:
		x = 0
		for i in Settings:
			print(f"{x} - {i}")
			x +=1
		print("X - Exit")
		choice = input("Choose option: ")
		if choice.lower() == "x":
			break
		else:
			a = list(Settings.keys())[int(choice)]
			if type(Settings[a]) is not (dict or list):
				Settings[a] = input(f"{a} - {Settings[a]}\nEnter new value : ")
			elif type(Settings[a]) is list:
				Settings[a] = input(f"{a} - {' '.join(Settings[a])}\nEnter new values (separated with spaces) : ").split(" ")
			elif type(Settings[a]) is dict:
				b = Settings[a]
				x = 0
				for i in b:
					print(f"{x} - {i}")
					x +=1
				print("X - Exit")
				choice = input("Choose option: ").title()
				if choice.lower() == "x":
					break
				else:
					a = list(b.keys())[int(choice)]
					if type(Settings['legal'][a]) is not (dict or list):
						Settings['legal'][a] = input(f"{a} - {' '.join(Settings['legal'][a])}\nEnter new value  (separated with spaces) : ").split(" ")
					elif type(Settings['legal'][a]) is list:
						Settings['legal'][a] = input(f"{a} - {' '.join(Settings['legal'][a])}\nEnter new values (separated with spaces) : ").split(" ")

				
				
if __name__ == "__main__":
	main()