from nltk.tokenize import word_tokenize
import spacy


"""
->Take an input text/Array text and tokenize the words
-------------------------------------------------------
Input : text/array of text
Output : array of words/Array of array of words
Library : nltk, spacy, regex
Language : french, english
-------------------------------------------------------
"""

class Worder:

	AvailableLanguage = ["french", "english"]
	AvailableLibrary = ["nltk","spacy","regex"]

	def __init__(self,lib,language):
		self.lib = lib
		self.language = language

		self.spacyLanguages = {}
		#french
		self.spacyLanguages["french"]="fr_core_news_sm"
		self.spacyLanguages["english"]="en_core_web_sm"

	def tokenize(self,text):
		if self.lib == "nltk":
			res = word_tokenize(text,language=self.language)

		elif self.lib == "spacy":
			nlp =spacy.load(self.spacyLanguages[self.language])
			doc = nlp(text)
			res = [x.text for x in doc]

		else:
			res=[]

		return res


if __name__ == "__main__":
	w = Worder("nltk", "french")
	text= "Salut je m'appelle Jean Louis et je suis un fifou aujourd'hui mais aussi jusqu'à demain"
	print(w.tokenize(text))
	w.lib="spacy"
	print(w.tokenize(text))

