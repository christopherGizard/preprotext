from tkinter import *

class PresentationFrame(Frame):
	def __init__(self, master):
		Frame.__init__(self, master, width=550,height=450)
		self.pack(fill="both")

		#Frame
		labelF = LabelFrame(self, text = "Welcome")
		labelF.pack(side ="top", fill="both",expand="yes", padx=5, pady=5)

		buttonF = Frame(self)
		buttonF.pack(side="bottom", fill="both",padx=5, pady=5)
		
		#Widget
		button = Button(buttonF, text ="Continue")
		button.pack(side="right")

		label = Label(labelF,text="""Welcome to preprotext tool.
This tool is very useful when it comes to text prepocessing.
Select the text file you want to clean and then select the cleaning parameters.
With this tool you can do the following :
-Sentences detection-
-Word tokenizer-
-Stop words suppression-
-Lemmatisation-
-Specific words removal-
-punctuation suppression-
-custom regex rules-""")
		label.pack()

		check = Checkbutton(buttonF, text="Stop showing me this page")
		check.pack(side="left")
