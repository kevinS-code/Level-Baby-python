#Ring.ry
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Volume of Ring volume')
########Funtion#########
def CR():
	R = float(RingRadiusS.get())
	r = float(RingRadiusB.get())
	Ans = 3.14*(R**2-r**2)
	RingShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
RingRadiusS = StringVar()
RingRadiusB = StringVar()
RingShowResalut = StringVar()
RingShowResalut.set('----------')
########################
RingLabel = ttk.Label(GUI,text='Calculate of Ring')
RingLabel.pack()

RingEntry = ttk.Entry(GUI,textvariable=RingRadiusS,font=FONT)
RingEntry.pack()

RingEntryH = ttk.Entry(GUI,textvariable=RingRadiusB,font=FONT)
RingEntryH.pack()

RingButton = ttk.Button(GUI,text='Calculate',command=CR)
RingButton.pack()

RingLabel1 = ttk.Label(GUI,textvariable=RingShowResalut,font=FONT)
RingLabel1.pack()

GUI.mainloop()
