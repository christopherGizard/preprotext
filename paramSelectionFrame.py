from tkinter import *
from tkinter.ttk import *

#from selectionFrame import SelectionFrame
from tools.nlp.sentencer import Sentencer
from tools.nlp.worder import Worder

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
		values = ['Sentencer','Word Tokenizer','Suppressor']
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
		sentencerLibraryListbox = Listbox(self.sentencerFrame,name='library',exportselection=False)
		for v in Sentencer.AvailableLibrary:
			sentencerLibraryListbox.insert('end',v)
		sentencerLibraryListbox.pack(side='left',padx=10,pady=10)
		sentencerLibraryListbox.bind('<<ListboxSelect>>', lambda event: self.set_options(event, "library"))

		sentencerLanguageListbox = Listbox(self.sentencerFrame,name='language',exportselection=False)
		for v in Sentencer.AvailableLanguage:
			sentencerLanguageListbox.insert('end',v)
		sentencerLanguageListbox.pack(side='right',padx=10,pady=10)
		sentencerLanguageListbox.bind('<<ListboxSelect>>',  lambda event: self.set_options(event, "language"))

		#Worder Options
		self.worderFrame = Frame(self.optFrame)
		worderLibraryListbox = Listbox(self.worderFrame,name='library',exportselection=False)
		for v in Worder.AvailableLibrary:
			worderLibraryListbox.insert('end',v)
		worderLibraryListbox.pack(side='left',padx=10,pady=10)
		worderLibraryListbox.bind('<<ListboxSelect>>', lambda event: self.set_options(event, "library"))

		worderLanguageListbox = Listbox(self.worderFrame,name='language',exportselection=False)
		for v in Worder.AvailableLanguage:
			worderLanguageListbox.insert('end',v)
		worderLanguageListbox.pack(side='right',padx=10,pady=10)
		worderLanguageListbox.bind('<<ListboxSelect>>',  lambda event: self.set_options(event, "language"))


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

	def clean_options(self):
		self.options = {}
		self.sentencerFrame.pack_forget()
		self.worderFrame.pack_forget()


	def change_options(self,evt):
		w = evt.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		if value == "Sentencer":
			self.clean_options()
			self.sentencerFrame.pack()
		elif value =="Word Tokenizer":
			self.clean_options()
			self.worderFrame.pack()
		else :
			self.clean_options()

	def set_options(self,evt,name):
		w=evt.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		self.options[name]=value












		




