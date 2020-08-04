
import tkinter as tk
#Local import
from presentationFrame import *

class PreProApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.frame = None
		self.switch_frame(PresentationFrame)

	def switch_frame(self,frame_class):
		new_frame = frame_class(self)
		if self.frame is not None:
			self.frame.destroy()
		self.frame = new_frame
		self.frame.pack()

if __name__ == "__main__":
    app = PreProApp()
    app.mainloop()