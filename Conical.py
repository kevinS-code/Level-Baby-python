#Conical.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Volume of Conical volume')
########Funtion#########
def CCO():
	COR = float(ConicalRadius.get())
	COH = float(ConicalHight.get())
	Ans = 1/3*3.14*COR**2*COH
	ConicalShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
ConicalRadius = StringVar()
ConicalHight = StringVar()
ConicalShowResalut = StringVar()
ConicalShowResalut.set('----------')
########################
ConicalLabel = ttk.Label(GUI,text='Calculate of Conical')
ConicalLabel.pack()

ConicalEntry = ttk.Entry(GUI,textvariable=ConicalRadius,font=FONT)
ConicalEntry.pack()

ConicalEntryH = ttk.Entry(GUI,textvariable=ConicalHight,font=FONT)
ConicalEntryH.pack()

ConicalButton = ttk.Button(GUI,text='Calculate',command=CCO)
ConicalButton.pack()

ConicalLabel1 = ttk.Label(GUI,textvariable=ConicalShowResalut,font=FONT)
ConicalLabel1.pack()

GUI.mainloop()