#Cylinder.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Volume of Cylinder volume')
########Funtion#########
def CCY():
	CYR = float(CylinderRadius.get())
	CYH = float(CylinderHight.get())
	Ans =(3.14*CYR**2)*CYH
	CylinderShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
CylinderRadius = StringVar()
CylinderHight = StringVar()
CylinderShowResalut = StringVar()
CylinderShowResalut.set('----------')
########################
CylinderLabel = ttk.Label(GUI,text='Calculate of Cylinder')
CylinderLabel.pack()

CylinderEntry = ttk.Entry(GUI,textvariable=CylinderRadius,font=FONT)
CylinderEntry.pack()

CylinderEntryH = ttk.Entry(GUI,textvariable=CylinderHight,font=FONT)
CylinderEntryH.pack()

CylinderButton = ttk.Button(GUI,text='Calculate',command=CCY)
CylinderButton.pack()

CylinderLabel1 = ttk.Label(GUI,textvariable=CylinderShowResalut,font=FONT)
CylinderLabel1.pack()

GUI.mainloop()