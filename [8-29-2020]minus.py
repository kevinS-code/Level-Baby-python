#minus.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Minus')
########Funtion#########
def Mi():
	Mi = float(Mi1.get())
	mi = float(Mi2.get())
	Ans = Mi-mi
	MiShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
Mi1 = StringVar()
Mi2 = StringVar()
MiShowResalut = StringVar()
MiShowResalut.set('----------')
########################
MiLabel = ttk.Label(GUI,text='Minus')
MiLabel.pack()

MiEntry = ttk.Entry(GUI,textvariable=Mi1,font=FONT)
MiEntry.pack()

MiEntryH = ttk.Entry(GUI,textvariable=Mi2,font=FONT)
MiEntryH.pack()

MiButton = ttk.Button(GUI,text='Calculate',command=Mi)
MiButton.pack()

MiLabel1 = ttk.Label(GUI,textvariable=MiShowResalut,font=FONT)
MiLabel1.pack()

GUI.mainloop()
