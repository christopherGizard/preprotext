from tkinter import *
from tkinter.ttk import *

#from selectionFrame import SelectionFrame

class ParamSelectionFrame(Frame):
	def __init__(self, master):
		Frame.__init__(self, master,width=550,height=450)

		self.parameters = []

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

		add = Button(rightFrame,text='Add',command=self.createNewWindow)
		add.pack(padx=5,pady=10)

		delete = Button(rightFrame,text='Delete')
		delete.pack(padx=5,pady=10)

		reset = Button(rightFrame,text='Reset')
		reset.pack(padx=5,pady=10)

		#from selectionFrame import SelectionFrame
		returnButton = Button(buttonF,text='Return to file selection',command=lambda: master.previous_frame())
		returnButton.pack(side ='left',padx=5,pady=5)

		nextButton = Button(buttonF,text='Next',state='disabled')
		nextButton.pack(side='right',padx=5,pady=5)

	def createNewWindow(self):
		newWindow = Toplevel(self)
		




