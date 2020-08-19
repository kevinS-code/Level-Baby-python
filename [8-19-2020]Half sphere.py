#Half sphere.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Volume of Half sphere volume')
########Funtion#########
def CHS():
	r = float(HalfsphereRadius.get())
	Ans = 2*3.142*r**3
	HalfsphereShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
HalfsphereRadius = StringVar()
HalfsphereShowResalut = StringVar() 
HalfsphereShowResalut.set('----------')
########################
HalfsphereLabel = ttk.Label(GUI,text='Calculate of Half sphere')
HalfsphereLabel.pack()

HalfsphereEntry = ttk.Entry(GUI,textvariable=HalfsphereRadius,font=FONT)
HalfsphereEntry.pack()

HalfsphereButton = ttk.Button(GUI,text='Calculate',command=CHS)
HalfsphereButton.pack()

HalfsphereLabel1 = ttk.Label(GUI,textvariable=HalfsphereShowResalut,font=FONT)
HalfsphereLabel1.pack()

GUI.mainloop()
