from nltk.tokenize import sent_tokenize
import spacy

"""
->Take an input text and return an array of the sentences of this text
-----------------------------------------------------------------------
Input : text
Output : Array of sentences
Library : Spacy, nltk
Language : French, English
-----------------------------------------------------------------------
"""

class Sentencer:
	#List of available language
	AvailableLanguage = ['english','french']
	#List of available library
	AvailableLibrary = ['nltk','spacy']

	def __init__(self,lib,language):
		self.lib=lib
		self.language=language
		#for spacy
		self.spacyLanguages = {}
		#french
		self.spacyLanguages["french"]="fr_core_news_sm"
		self.spacyLanguages["english"]="en_core_web_sm"

	def tokenize(self, text):
		if self.lib == 'nltk':
			res = sent_tokenize(text,language = self.language)
		else :
			nlp =spacy.load(self.spacyLanguages[self.language])
			doc = nlp(text)
			res = [x.text for x in doc.sents]
		return res

if __name__ == "__main__":
	s =Sentencer('nltk','french')
	text="""Bonjour je m'appelle Mr.Durant et je suis content. Trois ans plus tard je suis toujours content. Mais la pas content"""
	print(s.tokenize(text))
	s.lib="spacy"
	print(s.tokenize(text))