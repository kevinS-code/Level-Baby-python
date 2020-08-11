#Spherical volume
from tkinter import *
from tkinter import ttk
#######Screen##########
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Volume of Spherical volume')
########Funtion#########
def CS():
	S = float(Spherical.get())
	Ans = 4/3*3.14*S**3
	SphericalShowResalut.set(f'Answer is: {Ans:,.2f}')
#######Variable#########
FONT = ('Angsana New',20)
Spherical = StringVar()
SphericalShowResalut = StringVar()
SphericalShowResalut.set('----------')
########################
SphericalLabel = ttk.Label(GUI,text='Calculate of Spherical')
SphericalLabel.pack()

SphericalEntry = ttk.Entry(GUI,textvariable=Spherical,font=FONT)
SphericalEntry.pack()

SphericalButton = ttk.Button(GUI,text='Calculate',command=CS)
SphericalButton.pack()

SphericalLabel1 = ttk.Label(GUI,textvariable=SphericalShowResalut,font=FONT)
SphericalLabel1.pack()

GUI.mainloop()
