#Multiplication.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Multiplication')
########Funtion#########
def M():
	M = float(M1.get())
	m = float(M2.get())
	Ans = M*m
	MShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
M1 = StringVar()
M2 = StringVar()
MShowResalut = StringVar()
MShowResalut.set('----------')
########################
MLabel = ttk.Label(GUI,text='Multiplication')
MLabel.pack()

MEntry = ttk.Entry(GUI,textvariable=M1,font=FONT)
MEntry.pack()

MEntryH = ttk.Entry(GUI,textvariable=M2,font=FONT)
MEntryH.pack()

MButton = ttk.Button(GUI,text='Calculate',command=M)
MButton.pack()

MLabel1 = ttk.Label(GUI,textvariable=MShowResalut,font=FONT)
MLabel1.pack()

GUI.mainloop()