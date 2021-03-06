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
	Cal1 = float(Kelvin0.get())
	Celsius0.set(Cal1 - 273.15)
	Fahrenheit0.set((Cal1 * 1.8) - 459.67)
	KelvinShow.set(f'Ans is: {Celsius0.set():,.2f}K')
	KelvinShow.place(x=200,y=150)
	KelvinShow1.set(f'Ans is: {Fahrenheit0.set():,.2f}°F')
	KelvinShow1.place(x=200,y=150)

def FC():
	Cal2 = float(Fahrenheit00.get())
	Celsius00.set((Cal2-32) / 1.8)
	Kelvin00.set((Cal2+459.67) * 5/9)
	FahrenheitShow.set(f'Ans is: {Celsius00.get():,.2f}°C')
	FahrenheitShow.place(x=200,y=150)
	FahrenheitShow1.set(f'Ans is: {Kelvin00.set():,.2f}K')
	FahrenheitShow1.place(x=200,y=150)

################################
############Variable############
FONT = ('Angsana New',20)
Celsius = StringVar()
Kelvin = StringVar()
Fahrenheit = StringVar()
##########KC##########
Celsius0 = StringVar()	
Kelvin0 = StringVar()	
Fahrenheit0 = StringVar()	
####################	
Celsius00 = StringVar()	
Kelvin00 = StringVar()	
Fahrenheit00 = StringVar()
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

Entry_Kelvin = ttk.Entry(F2,textvariable=Kelvin0,font=FONT)
Entry_Kelvin.pack()

Label_Celsius = ttk.Label(F2,textvariable=Celsius0,font=FONT)
Label_Celsius.pack()

Label_Fahrenheit1 = ttk.Label(F2,textvariable=Fahrenheit0,font=FONT)
Label_Fahrenheit1.pack()

KCM = ttk.Button(F2,text='Calculate',command=KC)
KCM.pack()

##################################
###########Widget Fahrenheit######
FahrenheitLabel = ttk.Label(F3,text='°F to °C and K',font=FONT)
FahrenheitLabel.pack()

Entry_Fahrenheit = ttk.Entry(F3,textvariable=Fahrenheit00,font=FONT)
Entry_Fahrenheit.pack()

Label_Celsius1 = ttk.Label(F3,textvariable=Celsius00,font=FONT)
Label_Celsius1.pack()

Label_Kelvin1 = ttk.Label(F3,textvariable=Kelvin00,font=FONT)
Label_Kelvin1.pack()

FCM = ttk.Button(F3,text='Calculate',command=FC)
FCM.pack()

##################################
#Last update 8/9/2020-10:58 AM-99% completed-Unfinished 
#ปัญหาส่วนแรก Line 123 เปลี่ยน GUI เป็น F2 จะลองดูต่อว่าถ้าลบตัวแปรที่เพิ่มมาจะยังมีผลไหม Update 8/9/2020-9:26 AM [มั่วเอาลืมดูเวลาตอนแก้ปัญหานี้เสร็จ]
#ลบตัวแปร 0 กับ 00 ออกมีผลให้ frame อื่นมีคำตอบ ของหน้า celsius(F1) ไปอยู่ใน Entry F2,F3 เพราะใช้ตัวแปรเดียวกัน 
#ต่อจากข้างบน- แต่ผลลัพธ์แบบนี้ก็ได้เพราะใส่่ค่า Celsius ใน F1 ก็จะได้คำตอบแต่ ใน F2,F3 ก็จะมีคำตอบใน F1 ไปโผล่ในช่อง Entry ของ F2,F3 แล้วก็จะโชว์ค่า K,°F,°C พร้อม ถ้าต้องการแบบนี้ก็ได้ 
#ต่อจากข้างบน-แต่ระบบตอนนี้จะฟ้องว่า TypeError: set() missing 1 required positional argument: 'value' ซึ่งตอนที่ทำอยู่นี้ยังหาวิธีแก้ไม่ได้ Update 8/9/2020-9:37 AM
#ปัญหาส่วนที่สอง คัวแปรเหมือนกันทำให้ คำตอบในแต่ละ frame เชื่อมถึงกัน จะลองใช้วิธีแก้ปัญหา 2 วิธี คือ
#1 จะลองเพิ่มตัวแปรเหมือนเดิม ด้วย 2 วิธี 1 จะเปลี่ยนแค่ตัวแปรใน Cal,Cal1,CAl2 และ Entry ในแต่ละ widget แค่ของ K และ °F แต่คาดว่าน่าจะโชว์คำตอบอยู่เพราะไม่ได้เปลี่ยนตัวแปร 
#วิธีที่ 2 เปลี่ยนตัวแปรทั้งหมด ใน widget K กับ °F กับ def KC และ def FC คาดว่าน่าจะได้ผลลัพธ์ตามที่คาดไว้ตือใก้แต่ละ frame ไม่เชื่อมกัน
#วิธีที่ 1 คำตอบใน F1 ไม่เด้งไปในช่อง Entry แต่โชว์ผลลัพธ์ของ K,°F,°C อยู่ตามคาด วิธีที่ 2 ผลลัพธ์ คำตอบในแต่ละ frame แยกจากกันไม่เชื่อมถึงกันแล้ว ตามที่คาดไว้ Update 8/9/2020-10:57 AM
#2 จะลองลบ global ดู ผลลัพธ์ ลบตัวแปร global ออกทั้งหมด ไม่มีผลกับการทำงานของโปรแกรม แต่ยังมีปัญหาอยู่2เรื่อง เรื่องแรก คำตอบในแต่ละ frame ยังเชื่อมถึงกันอยู่[ลองเอากลับมาดูแล้วรันได้จึงค่อยใส่กรอบแล้วจึงมีข้อความนี้[เรื่องที่สอง ที่อยู่หรือตำแหน่งของค่า 'value'  Update 8/9/2020-10:03 AM]] 
#เรื่องที่สอง ที่อยู่หรือตำแหน่งของค่า 'value'  Update 8/9/2020-10:11 AM (ตอนที่มีปัญหาคือเวลาเป็น 10:03 AM)(ไม่รู้เกี่ยวไหม+กันลืม)
#(ไม่รู้เกี่ยวไหมแต่เมื่อกี่ตอนเพิ่มข้อมูลใน #1 แล้ว Save พอจะลองรันดันขึ้นว่ามีปัญหาตรง Line 134 เลยงงว่า # อยู่มีปัญหาได้ไง เลยลองอ่านแต่ก็ไม่รู้ปัญหาคืออะไรเลยคิดไปเองว่าน่าจะยาวเกินไปเลย เลย Enter ลงมาสรุปรันต่อได้ คาดว่าอาจจะไปซ้ำกับคำสั่งหรือภาษาคอมพิวเตอร์หรือภาษาของ python หรือรูปแบบในการเขียนไม่ถูกต้อง)(ไม่รู้เกี่ยวไหม+กันลืม)
#เมื่อกี้ลองเอา #เรื่องที่สอง ขึ้นไปเหมือนเดิมสรุป)รันได้ ส่วนข้อความที่มีปัญหาเดี่ยวอัพขึ้น gidhub--update 8/9/2020 10:33 AM 
#ปัญหาส่วนสุดท้าย TypeError: set() missing 1 required positional argument: 'value' ไม่มีผลกับการทำงานของโปนแกรม แต่ก็จะหาวิธีแก้ดู
##################################
GUI.mainloop() 
