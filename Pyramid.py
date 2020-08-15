#pyramid.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Volume of pyramid volume')
########Funtion#########
def CP():
	PB = float(pyramidBase.get())
	PH = float(pyramidHight.get())
	PS = float(pyramidSide.get())
	Ans = 1/3*PB*PH*PS**2
	pyramidShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
pyramidBase = StringVar()
pyramidHight = StringVar()
pyramidSide = StringVar()
pyramidShowResalut = StringVar()
pyramidShowResalut.set('----------')
########################
pyramidLabel = ttk.Label(GUI,text='Calculate of pyramid')
pyramidLabel.pack()

pyramidEntry = ttk.Entry(GUI,textvariable=pyramidBase,font=FONT)
pyramidEntry.pack()

pyramidEntryH = ttk.Entry(GUI,textvariable=pyramidHight,font=FONT)
pyramidEntryH.pack()

pyramidEntryS = ttk.Entry(GUI,textvariable=pyramidSide,font=FONT)
pyramidEntryS.pack()

pyramidButton = ttk.Button(GUI,text='Calculate',command=CP)
pyramidButton.pack()

pyramidLabel1 = ttk.Label(GUI,textvariable=pyramidShowResalut,font=FONT)
pyramidLabel1.pack()

GUI.mainloop()