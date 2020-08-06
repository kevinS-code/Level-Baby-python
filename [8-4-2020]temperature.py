#temperature.py
from tkinter import *
from tkinter import ttk

Celsius = None
Kelvin = None
Fahrenheit = None

GUI = Tk()
GUI.geometry('500x500')
GUI.title('แปลงอุณหภูมิ')

def All():

	global Celsius
	global Kelvin
	global Fahrenheit
	val =float(Celsius.get())
	Kelvin.set((val + 273.15 ))
	Fahrenheit.set((val * 1.8) + 32)
	AllAnswer.set(f'คำตอบ: {Kelvin.set():,.2f}')
	AllAnswer1.set(f'คำตอบ: {Fahrenheit.set():,.2f}')

#############################

FONT = ('Angsana New',20)
Celsius = StringVar()
Kelvin = StringVar()
Fahrenheit = StringVar()
AllAnswer = StringVar()
AllAnswer.set('----------')
AllAnswer1 = StringVar()
AllAnswer1.set('----------')

CelsiusLable1 = ttk.Label(GUI,text='โปรแกรมแปลงค่าอุณหภูมิ',font=FONT)
CelsiusLable1.pack()

Entry_Celsius1 = ttk.Entry(GUI,textvariable=Celsius,font=FONT)
Entry_Celsius1.pack()

Label_Kelvin = ttk.Label(GUI,textvariable=Kelvin,font=FONT)
Label_Kelvin.pack()

Label_Fahrenheit = ttk.Label(GUI,textvariable=Fahrenheit,font=FONT)
Label_Fahrenheit.pack()

AllB1 = ttk.Button(GUI,text='คำนวณ',command=All)
AllB1.pack()

GUI.mainloop() #Last update 8/5/2020
