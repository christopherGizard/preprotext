from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from tools.fileAnalyser import *
from paramSelectionFrame import ParamSelectionFrame

class SelectionFrame(Frame):
	def __init__(self,master):
		self.selection=[]

		Frame.__init__(self, master, width=550,height=450)
		self.pack(fill="both")

		#Frame
		selectFrame = LabelFrame(self,text="Text File Selection")
		selectFrame.pack(side="top",fill="both",padx=5,pady=5)

		tabFrame = LabelFrame(self,text = "Selected Text")
		tabFrame.pack(padx=5,pady=5)

		buttonFrame = Frame(self)
		buttonFrame.pack()

		#Widget
		lab1 = Label(selectFrame,text="Select the text file you want to clean")
		lab1.pack()

		self.tab = Treeview(tabFrame, columns=('Text File Name', 'Text File Path', 'Extension', 'Size', 'Words','Lines'))
		self.tab.heading('Text File Name', text='Text File Name')
		self.tab.column('Text File Name',width=90,anchor="center")
		self.tab.heading('Text File Path', text='Text File Path')
		self.tab.heading('Extension', text='Extension')
		self.tab.column('Extension',width=60,anchor="center")
		self.tab.heading('Size', text='Size')
		self.tab.column('Size',width=60,anchor="center")
		self.tab.heading('Words', text='Words')
		self.tab.column('Words',width=60,anchor="center")
		self.tab.heading('Lines', text='Lines')
		self.tab.column('Lines',width=60,anchor="center")
		self.tab['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
		self.tab.pack(padx = 10, pady = (0, 10))


		resetButton = Button(buttonFrame, text="Reset files",command=self.reset)
		resetButton.pack(side="left",padx=5,pady=5)

		self.button = Button(buttonFrame,text="Next",state='disabled',command=lambda: master.switch_frame(ParamSelectionFrame))
		self.button.pack(side="right",padx=5,pady=5)

		selectButton = Button(selectFrame,text="Search",command=self.select_file)
		selectButton.pack()

	def select_file(self):
		filename =  filedialog.askopenfilename(initialdir = "Documents",title = "Select file")
		if filename :
			fa = FileAnalyser(filename)
			self.tab.insert('', 'end',values=(fa.name,fa.path,fa.ext,fa.size,fa.wordCount,fa.lineCount))
			self.selection.append((fa.name,fa.path,fa.ext,fa.size,fa.wordCount,fa.lineCount))
		if self.selection :
			self.button['state']='normal'

	def reset(self):
		self.selection=[]
		x = self.tab.get_children()
		for item in x:
			self.tab.delete(item)
		self.button['state']='disabled'