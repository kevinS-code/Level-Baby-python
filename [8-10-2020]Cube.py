#Cube.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Volume of Cube')
########Funtion#########
def CC():
	C = float(Cube.get())
	Ans = C**3
	CubeShowResalut.set(f'Answer is: {Ans:,.2f}')
########################
#######Variable#########
FONT = ('Angsana New',20)
Cube = StringVar()
CubeShowResalut = StringVar()
CubeShowResalut.set('----------')
########################
CubeLabel = ttk.Label(GUI,text='Calculate of Cube',font=FONT)
CubeLabel.pack()

CubeEntry = ttk.Entry(GUI,textvariable=Cube,font=FONT)
CubeEntry.pack()

CubeButton = ttk.Button(GUI,text='Calculate',command=CC)
CubeButton.pack()

CubeLabel1 = ttk.Label(GUI,textvariable=CubeShowResalut,font=FONT)
CubeLabel1.pack()

GUI.mainloop()
