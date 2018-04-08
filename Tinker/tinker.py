#!/usr/bin/python

import tkinter
#import tkMessageBox

top = tkinter.Tk()

print ("HELLO WORLD................")




def helloResponse():
	tkMessageBox.showinfo("Hello PY", "Hello Wolrd")

B = tkinter.Button(top, text = "Text", command = helloResponse)
B.pack()
top.mainloop()