#Spherical surface area.py
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Spherical surface area')
########Funtion#########
def CSSA():
	r = float(SphericalRadius.get())
	Ans = 4*3.142*r**2
	SphericalShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
SphericalRadius = StringVar()
SphericalShowResalut = StringVar() 
SphericalShowResalut.set('----------')
########################
SphericalLabel = ttk.Label(GUI,text='Calculate of Spherical')
SphericalLabel.pack()

SphericalEntry = ttk.Entry(GUI,textvariable=SphericalRadius,font=FONT)
SphericalEntry.pack()

SphericalButton = ttk.Button(GUI,text='Calculate',command=CSSA)
SphericalButton.pack()

SphericalLabel1 = ttk.Label(GUI,textvariable=SphericalShowResalut,font=FONT)
SphericalLabel1.pack()

GUI.mainloop()
