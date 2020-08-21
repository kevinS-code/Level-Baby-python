#Hexagon.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Volume of Hexagon volume')
########Funtion#########
def CH():
	S = float(HexagonSide.get())
	Ans = 6*0.433*S**2
	HexagonShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
HexagonSide = StringVar()
HexagonShowResalut = StringVar() 
HexagonShowResalut.set('----------')
########################
HexagonLabel = ttk.Label(GUI,text='Calculate of Hexagon')
HexagonLabel.pack()

HexagonEntry = ttk.Entry(GUI,textvariable=HexagonSide,font=FONT)
HexagonEntry.pack()

HexagonButton = ttk.Button(GUI,text='Calculate',command=CH)
HexagonButton.pack()

HexagonLabel1 = ttk.Label(GUI,textvariable=HexagonShowResalut,font=FONT)
HexagonLabel1.pack()

GUI.mainloop()