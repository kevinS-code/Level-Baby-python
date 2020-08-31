#plus.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Plus')
########Funtion#########
def Pl():
	Pl = float(Pl1.get())
	pl = float(pl2.get())
	Ans = Pl+pl
	PlShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
Pl1 = StringVar()
pl2 = StringVar()
PlShowResalut = StringVar()
PlShowResalut.set('----------')
########################
PlLabel = ttk.Label(GUI,text='Plnus')
PlLabel.pack()

PlEntry = ttk.Entry(GUI,textvariable=Pl1,font=FONT)
PlEntry.pack()

PlEntryH = ttk.Entry(GUI,textvariable=pl2,font=FONT)
PlEntryH.pack()

PlButton = ttk.Button(GUI,text='Calculate',command=Pl)
PlButton.pack()

PlLabel1 = ttk.Label(GUI,textvariable=PlShowResalut,font=FONT)
PlLabel1.pack()

GUI.mainloop()
