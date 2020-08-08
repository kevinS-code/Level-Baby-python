#temperature.py
from tkinter import *
from tkinter import ttk

Celsius = None
Kelvin = None
Fahrenheit = None
Celsius0 = None
Kelvin00 = None
Fahrenheit0 = None
Celsius00 = None
Kelvin00 = None
Fahrenheit00 = None

############Screen##############
GUI = Tk()
GUI.geometry('500x500')
GUI.title('แปลงอุณหภูมิ  °C to K and °F')
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH)
F1 = Frame(Tab)
F2 = Frame(Tab)
F3 = Frame(Tab)
Tab.add(F1,text='°C')
Tab.add(F2,text='K')
Tab.add(F3,text='°F')
############Function############
def All():

	global Celsius
	global Kelvin
	global Fahrenheit
	Cal = float(Celsius.get())
	Kelvin.set((Cal + 273.15 ))
	Fahrenheit.set((Cal * 1.8) + 32)
	Allanswer.set(f'คำตอบ: {Kelvin.set():,.2f}')
	Allanswer1.set(f'คำตอบ: {Fahrenheit.set():,.2f}')

def KC():

	global Kelvin00
	global Celsius0
	global Fahrenheit0
	Cal1 = float(Kelvin.get())
	Celsius0.set((Cal1 - 273.15))
	Fahrenheit0.set((Cal1 * 1.8) - 459.67)
	KelvinShow.set(f'Ans is: {Celsius.set():,.2f}')
	KelvinShow1.set(f'Ans is: {Fahrenheit.set():,.2f}')

def FC():

	global Fahrenheit00
	global Celsius00
	global Kelvin00
	Cal2 = float(Fahrenheit.get())
	Celsius00.set((Cal2-32) / 1.8)
	Kelvin00.set((Cal2+459.67) * 5/9)
	FahrenheitShow.set(f'Ans is: {Celsius.get():,.2f}')
	FahrenheitShow1.set(f'Ans is: {Kelvin.set():,.2f}')

################################
############Variable############
FONT = ('Angsana New',20)
Celsius = StringVar()
Kelvin = StringVar()
Fahrenheit = StringVar()
########ALL###########
Celsius0 = StringVar()
Kelvin0 = StringVar()
Fahrenheit0 = StringVar()
#######KC#############
Celsius00 = StringVar()
Kelvin00 = StringVar()
Fahrenheit00 = StringVar()
########FC############
Allanswer = StringVar()
Allanswer.set('----------')
Allanswer1 = StringVar()
Allanswer1.set('----------')
######Kelvin###########
KelvinShow = StringVar()
KelvinShow.set('-----------')
KelvinShow1 = StringVar()
KelvinShow1.set('-----------')
######Fahrenheit#######
FahrenheitShow = StringVar()
FahrenheitShow.set('-----------')
FahrenheitShow1 = StringVar()
FahrenheitShow1.set('-----------')
###########Widget Celsius##########
CelsiusLable = ttk.Label(F1,text='โปรแกรมแปลงค่าอุณหภูมิ',font=FONT)
CelsiusLable.pack()

Entry_Celsius = ttk.Entry(F1,textvariable=Celsius,font=FONT)
Entry_Celsius.pack()

Label_Kelvin = ttk.Label(F1,textvariable=Kelvin,font=FONT)
Label_Kelvin.pack()

Label_Fahrenheit = ttk.Label(F1,textvariable=Fahrenheit,font=FONT)
Label_Fahrenheit.pack()

AllB1 = ttk.Button(F1,text='คำนวณ',command=All)
AllB1.pack()

CelsiusResult = ttk.Label(F1,textvariable=Allanswer,font=FONT)
CelsiusResult.pack()

CelsiusResult1 = ttk.Label(F1,textvariable=Allanswer1,font=FONT)
CelsiusResult1.pack()
##################################
###########Widget Kelvin##########
KelvinLabel = ttk.Label(F2,text='K to °C and °F')
KelvinLabel.pack()

Entry_Kelvin = ttk.Entry(F2,textvariable=Kelvin,font=FONT)
Entry_Kelvin.pack()

Label_Celsius = ttk.Label(F2,textvariable=Celsius0,font=FONT)
Label_Celsius.pack()

Label_Fahrenheit1 = ttk.Label(GUI,textvariable=Fahrenheit0,font=FONT)
Label_Fahrenheit1.pack()

KCM = ttk.Button(F2,text='Calculate',command=KC)
KCM.pack()

KelvinResult = ttk.Label(F2,textvariable=KelvinShow,font=FONT)
KelvinResult.pack()

KelvinResult1 = ttk.Label(F2,textvariable=KelvinShow1,font=FONT)
KelvinResult1.pack()
##################################
###########Widget Fahrenheit######
FahrenheitLabel = ttk.Label(F3,text='°F to °C and K')
FahrenheitLabel.pack()

Entry_Fahrenheit = ttk.Entry(F3,textvariable=Fahrenheit,font=FONT)
Entry_Fahrenheit.pack()

Label_Celsius1 = ttk.Label(F3,textvariable=Celsius00,font=FONT)
Label_Celsius1.pack()

Label_Kelvin1 = ttk.Label(F3,textvariable=Kelvin00,font=FONT)
Label_Kelvin1.pack()

FCM = ttk.Button(F3,text='Calculatel',command=FC)
FCM.pack()

FahrenheitResult = ttk.Label(F3,textvariable=FahrenheitShow,font=FONT)
FahrenheitResult.pack()


FahrenheitResult1 = ttk.Label(F3,textvariable=FahrenheitShow1,font=FONT)
FahrenheitResult1.pack()
##################################
GUI.mainloop() #Last update 8/8/2020-7:33 PM Unfinished
