from tkinter import *
from tkinter.ttk import *

#from selectionFrame import SelectionFrame
from tools.nlp.sentencer import Sentencer

class ParamSelectionFrame(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,width=550,height=450)

		self.parameters = []
		self.options={}

		#Frame
		labelF = LabelFrame(self, text="Cleaning parameters")
		labelF.pack(side="top",padx=5,pady=5)

		tabFrame = Frame(labelF)
		tabFrame.pack(side='left')

		rightFrame = Frame(labelF)
		rightFrame.pack(side='right')

		buttonF = Frame(self)
		buttonF.pack(side="bottom",padx=5,pady=5)

		#Widget

		self.tab = Treeview(tabFrame, columns=('Filter', 'Options'))
		self.tab.heading('Filter', text='Filter')
		self.tab.column('Filter',width=90,anchor="center")
		self.tab.heading('Options', text='Options')
		self.tab.column('Options',anchor="center")
		self.tab['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
		self.tab.pack(side = 'left',padx = 10, pady = (0, 10))

		add = Button(rightFrame,text='Add',command=self.add_param)
		add.pack(padx=5,pady=10)

		delete = Button(rightFrame,text='Delete',command=self.delete_filter)
		delete.pack(padx=5,pady=10)

		reset = Button(rightFrame,text='Reset',command=self.reset_filter)
		reset.pack(padx=5,pady=10)

		
		returnButton = Button(buttonF,text='Return to file selection',command=lambda: master.previous_frame())
		returnButton.pack(side ='left',padx=5,pady=5)

		self.nextButton = Button(buttonF,text='Next',state='disabled')
		self.nextButton.pack(side='right',padx=5,pady=5)

	def add_param(self):
		self.window = Toplevel(self)
		self.window.grab_set()
		
		#Frame
		topFrame = Frame(self.window)
		topFrame.pack(side='top')

		bottomFrame = Frame(self.window)
		bottomFrame.pack(side='bottom')

		filFrame = LabelFrame(topFrame,text='Filter')
		filFrame.pack(side='top',padx=5,pady=5)

		self.optFrame = LabelFrame(topFrame,text='Options')
		self.optFrame.pack(side='bottom', padx=5, pady=5)

		#Widget
		listboxLabel = Label(filFrame,text="Choose your filter")
		listboxLabel.pack(side="top")

		self.listbox = Listbox(filFrame,exportselection=False)
		values = ['Sentencer','Word Tokenizer','Stop Words Suppression','Punctuation Suppression','LowerCase Text','Lemming','Stemming','Custom Words Removal','Custom Regex']
		for v in values:
			if v not in self.parameters:
				self.listbox.insert('end',v)
		self.listbox.pack(padx=5,pady=5)
		self.listbox.bind('<<ListboxSelect>>', self.change_options)


		addFilterButton = Button(bottomFrame,text='Add Filter',command=self.add_filter)
		addFilterButton.pack(side="right",padx=5,pady=5)

		closeButton = Button(bottomFrame,text='Close',command=self.window.destroy)
		closeButton.pack(side='left',padx=5,pady=5)

		#Sentencer Options
		self.sentencerFrame = Frame(self.optFrame)
		libraryListbox = Listbox(self.sentencerFrame,name='library',exportselection=False)
		for v in Sentencer.AvailableLibrary:
			libraryListbox.insert('end',v)
		libraryListbox.pack(side='left',padx=10,pady=10)
		libraryListbox.bind('<<ListboxSelect>>', lambda event: self.set_options(event, "library"))

		languageListbox = Listbox(self.sentencerFrame,name='language',exportselection=False)
		for v in Sentencer.AvailableLanguage:
			languageListbox.insert('end',v)
		languageListbox.pack(side='right',padx=10,pady=10)
		languageListbox.bind('<<ListboxSelect>>',  lambda event: self.set_options(event, "language"))

		#Add,delete and reset filters
	def add_filter(self):
		if self.listbox.get(ACTIVE) :
			self.parameters.append(self.listbox.get(ACTIVE))
			self.tab.insert('', 'end',values=(self.listbox.get(ACTIVE),self.options))
			self.window.grab_release()
			self.window.destroy()
		if self.parameters:
			self.nextButton['state']='normal'

	def delete_filter(self):
		if self.tab.selection():
			selected = self.tab.selection()
			for s in selected :
				self.parameters.remove(self.tab.item(s)['values'][0])
				self.tab.delete(s)

		if not self.parameters :
			self.nextButton['state']='disabled'

	def reset_filter(self):
		self.parameters=[]
		x = self.tab.get_children()
		for item in x:
			self.tab.delete(item)
		self.nextButton['state']='disabled'


	def change_options(self,evt):
		w = evt.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		if value == "Sentencer":
			self.sentencerFrame.pack()
		else :
			self.options ={}
			self.sentencerFrame.pack_forget()

	def set_options(self,evt,name):
		w=evt.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		self.options[name]=value












		




