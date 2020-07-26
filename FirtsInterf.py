from tkinter import *

root = Tk() #create root

firstframe= Frame(root,width=1200, height=600) #create frame 1200x6000
firstframe.pack()

boxname=Entry(firstframe)
boxname.grid(row=0,column=1)

name = Label(firstframe,text="Nombre")
name.grid(row=0,column=0)

boxdir=Entry(firstframe)
boxdir.grid(row=1,column=1)

dir = Label(firstframe,text="Dirección")
dir.grid(row=1,column=0)







root.mainloop()

