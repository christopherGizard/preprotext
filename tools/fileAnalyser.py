import os

class FileAnalyser:
	def __init__(self,filepath):
		self.path = filepath
		lines=0
		words=0
		with open(filepath,'r') as file:
			for line in file.readlines():
				for word in line.strip():
					words+=1
				lines+=1
		self.wordCount=words
		self.lineCount=lines
		self.size = os.stat(self.path).st_size
		self.name=self.path.split('/')[-1]
		self.ext=self.name.split('.')[-1]

	def __repr__(self):
		return self.path +"\n"+self.name+"\n"+self.ext+"\n"+str(self.size)+"\n"+str(self.wordCount)+"\n"+str(self.lineCount)

		
if __name__ == "__main__":
	f = FileAnalyser("C:/Users/Christopher/Documents/Machine Learning/NLP/Problemes NLP.txt")
	print(f)