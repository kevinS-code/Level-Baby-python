#cone.py
from tkinter import *
from tkinter import ttk 

GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมคำนวณปริมาตรทรงกรวย')

def Cone():
	f = float(F.get())
	h = float(H.get())
	Ans = 1/3 * f * h
	SW.set(f'คำตอบคือ {Ans:,.2f}')

FONT = ('Angsana New',20)
F = StringVar()
H = StringVar()
SW = StringVar()
SW.set('-------')

L1 = ttk.Label(GUI,text='โปรแกรมคำนวณปริมาตรทรงกรวย',font=FONT)
L1.pack()

E1 = ttk.Entry(GUI,textvariable=F,font=FONT)
E1.pack()

E2 = ttk.Entry(GUI,textvariable=H,font=FONT)
E2.pack()

B1 = ttk.Button(GUI,text='คำนวณ',command=Cone)
B1.pack()

SW.L = ttk.Label(GUI,textvariable=SW,font=FONT)
SW.L.pack()

GUI.mainloop()
