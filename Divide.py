#Divide.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Divide')
########Funtion#########
def D():
	D = float(D1.get())
	d = float(D2.get())
	Ans = D/d
	DShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
D1 = StringVar()
D2 = StringVar()
DShowResalut = StringVar()
DShowResalut.set('----------')
########################
DLabel = ttk.Label(GUI,text='Divide')
DLabel.pack()

DEntry = ttk.Entry(GUI,textvariable=D1,font=FONT)
DEntry.pack()

DEntryH = ttk.Entry(GUI,textvariable=D2,font=FONT)
DEntryH.pack()

DButton = ttk.Button(GUI,text='Calculate',command=D)
DButton.pack()

DLabel1 = ttk.Label(GUI,textvariable=DShowResalut,font=FONT)
DLabel1.pack()

GUI.mainloop()