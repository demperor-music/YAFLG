import random, itertools

class WordGen:
	def SyllableGen(legal: dict):
		SyllableList = list()
		Syllable = str()
		for i in legal["Syllable Structures"]:
			comb = []
			for y in i:
				comb += [legal[y.upper()]]
			# legal[y.upper()] for y in i
			Syllable = itertools.product(*comb)
			Syllable = list(Syllable)
			h = []
			for i in Syllable:
				h += ["".join(i)]
			SyllableList += h
		return sorted(SyllableList)
	
	def WordGen(Syllables:list, length:int):
		word = str()
		for i in range(length):
			word += random.choice(Syllables)
		return word

	def WordList(n, minlength, maxlength, Syllables):
		L = []
		for i in range(n):
			L += [WordGen.WordGen(Syllables, random.randint(minlength,maxlength))]
		return L
