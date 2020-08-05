
import tkinter as tk
#Local import
from presentationFrame import *
from selectionFrame import *

class PreProApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.frame = None
		self.previousFrame = None
		self.switch_frame(PresentationFrame)

	def switch_frame(self,frame_class):
		new_frame = frame_class(self)
		if self.frame is not None:
			self.previousFrame =self.frame
			self.frame.pack_forget()
		self.frame = new_frame
		self.frame.pack()
		

	def previous_frame(self):
		if self.previousFrame is not None:
			self.frame.pack_forget()
			self.frame = self.previousFrame
			self.frame.pack()


if __name__ == "__main__":
    app = PreProApp()
    app.mainloop()