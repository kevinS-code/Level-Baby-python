#temperature.py
from tkinter import *
from tkinter import ttk

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

	
	Cal = float(Celsius.get())
	Kelvin.set((Cal + 273.15 ))
	Fahrenheit.set((Cal * 1.8) + 32)
	Allanswer.set(f'คำตอบ: {Kelvin.set():,.2f}K')
	Allanswer.place(x=200,y=150)
	Allanswer1.set(f'คำตอบ: {Fahrenheit.set():,.2f}°F')
	Allanswer1.place(x=200,y=150)

def KC():


	Cal1 = float(Kelvin.get())
	Celsius.set(Cal1 - 273.15)
	Fahrenheit.set((Cal1 * 1.8) - 459.67)
	KelvinShow.set(f'Ans is: {Celsius.set():,.2f}K')
	KelvinShow.place(x=200,y=150)
	KelvinShow1.set(f'Ans is: {Fahrenheit.set():,.2f}°F')
	KelvinShow1.place(x=200,y=150)

def FC():

	
	Cal2 = float(Fahrenheit.get())
	Celsius.set((Cal2-32) / 1.8)
	Kelvin.set((Cal2+459.67) * 5/9)
	FahrenheitShow.set(f'Ans is: {Celsius.get():,.2f}°C')
	FahrenheitShow.place(x=200,y=150)
	FahrenheitShow1.set(f'Ans is: {Kelvin.set():,.2f}K')
	FahrenheitShow1.place(x=200,y=150)

################################
############Variable############
FONT = ('Angsana New',20)
Celsius = StringVar()
Kelvin = StringVar()
Fahrenheit = StringVar()
########ALL###########
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
CelsiusLable = ttk.Label(F1,text='โปรแกรมแปลงค่าอุณหภูมิ °C to K and °F',font=FONT)
CelsiusLable.pack()

Entry_Celsius = ttk.Entry(F1,textvariable=Celsius,font=FONT)
Entry_Celsius.pack()

Label_Kelvin = ttk.Label(F1,textvariable=Kelvin,font=FONT)
Label_Kelvin.pack()

Label_Fahrenheit = ttk.Label(F1,textvariable=Fahrenheit,font=FONT)
Label_Fahrenheit.pack()

AllB1 = ttk.Button(F1,text='คำนวณ',command=All) #คำนวณ ภาษาอังกฤษคือคำว่า Calculate
AllB1.pack()

##################################
###########Widget Kelvin##########
KelvinLabel = ttk.Label(F2,text='K to °C and °F',font=FONT)
KelvinLabel.pack()

Entry_Kelvin = ttk.Entry(F2,textvariable=Kelvin,font=FONT)
Entry_Kelvin.pack()

Label_Celsius = ttk.Label(F2,textvariable=Celsius,font=FONT)
Label_Celsius.pack()

Label_Fahrenheit1 = ttk.Label(F2,textvariable=Fahrenheit,font=FONT)
Label_Fahrenheit1.pack()

KCM = ttk.Button(F2,text='Calculate',command=KC)
KCM.pack()

##################################
###########Widget Fahrenheit######
FahrenheitLabel = ttk.Label(F3,text='°F to °C and K',font=FONT)
FahrenheitLabel.pack()

Entry_Fahrenheit = ttk.Entry(F3,textvariable=Fahrenheit,font=FONT)
Entry_Fahrenheit.pack()

Label_Celsius1 = ttk.Label(F3,textvariable=Celsius,font=FONT)
Label_Celsius1.pack()

Label_Kelvin1 = ttk.Label(F3,textvariable=Kelvin,font=FONT)
Label_Kelvin1.pack()

FCM = ttk.Button(F3,text='Calculate',command=FC)
FCM.pack()

##################################
#Last update 8/9/2020-9:16 AM Unfinished 
#ปัญหาส่วนแรก Line 123 เปลี่ยน GUI เป็น F2 จะลองดูต่อว่าถ้าลบตัวแปรที่เพิ่มมาจะยังมีผลไหม Update 8/9/2020-9:26 AM [มั่วเอาลืมดูเวลาตอนแก้ปัญหานี้เสร็จ]
#ลบตัวแปร 0 กับ 00 ออกมีผลให้ frame อื่นมีคำตอบ ของหน้า celsius(F1) ไปอยู่ใน Entry F2,F3 เพราะใช้ตัวแปรเดียวกัน 
#ต่อจากข้างบน- แต่ผลลัพธ์แบบนี้ก็ได้เพราะใส่่ค่า Celsius ใน F1 ก็จะได้คำตอบแต่ ใน F2,F3 ก็จะมีคำตอบใน F1 ไปโผล่ในช่อง Entry ของ F2,F3 แล้วก็จะโชว์ค่า K,°F,°C พร้อม ถ้าต้องการแบบนี้ก็ได้ 
#ต่อจากข้างบน-แต่ระบบตอนนี้จะฟ้องว่า TypeError: set() missing 1 required positional argument: 'value' ซึ่งตอนที่ทำอยู่นี้ยังหาวิธีแก้ไม่ได้ Update 8/9/2020-9:37 AM
#ปัญหาส่วนที่สอง คัวแปรเหมือนกันทำให้ คำตอบในแต่ละ frame เชื่อมถึงกัน จะลองใช้วิธีแก้ปัญหา 2 วิธี คือ
#1 จะลองเพิ่มตัวแปรเหมือนเดิม
#2 จะลองลบ global ดู ผลลัพธ์ ลบตัวแปร global ออกทั้งหมด ไม่มีผลกับการทำงานของโปรแกรม แต่ยังมีปัญหาอยู่2เรื่อง เรื่องแรก คำตอบในแต่ละ frame ยังเชื่อมถึงกันอยู่ เรื่องที่สอง ที่อยู่หรือตำแหน่งของค่า 'value'  Update 8/9/2020-10:03 AM
##################################
GUI.mainloop() 
