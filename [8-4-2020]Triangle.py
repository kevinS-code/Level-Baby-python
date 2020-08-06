#Triangle.py
from tkinter import *
from tkinter import ttk

BG = Tk()
BG.geometry('500x500')
BG.title('โปรแกรมคำนวณพื้นที่สามเหลี่ยม')

def TA():
	f = float(F.get())
	h = float(H.get())
	Ans = 1/2 * f * h
	Answer.set(f'คำตอบคือ: {Ans:,.2f}')


FONT = ('Angsana New',20)
F = StringVar()
H = StringVar()
Answer = StringVar()
Answer.set('----------')

TAL1 = ttk.Label(BG,text='โปรแกรมคำนวณพื้นที่ สามเหลี่ยม',font=FONT)
TAL1.pack(pady=50)

TAE1 = ttk.Entry(BG,textvariable=F,font=FONT)
TAE1.pack(ipadx=10,ipady=5,padx=3,pady=3)

TAE2 = ttk.Entry(BG,textvariable=H,font=FONT)
TAE2.pack(ipadx=10,ipady=5,padx=3,pady=3)

TAB1 = ttk.Button(BG,text='คำนวณ',command=TA)
TAB1.pack(ipadx=10,ipady=5,padx=3,pady=3)

TAL2 = ttk.Label(BG,textvariable=Answer,font=FONT)
TAL2.pack()

BG.mainloop()
