#Project1st.py
from tkinter import * 
from tkinter import ttk,messagebox #(Date:8/3/2020)

def Calcurate():
	input1 = int(value1.get())
	input2 = int(value2.get())
	res = input1 + input2
	result.set(f'คำตอบคือ {res:,d}')#(Date:8/3/2020)

'''def CalcuratE():
	input1 = int(value1.get())
	input2 = int(value2.get())
	ser = input1 + input2
	Result.set(f'คำตอบคือ {ser:,d}')'''#(Date:8/3/2020)

def Plus():
	messagebox.showinfo('วิธีบวก','นี่คือตัวอย่าง 1 + 1 = 2')
def Minus():
	messagebox.showinfo('วิธีลบ','นี่คือตัวอย่าง 1 - 1 = 0')
def Multiple():
	messagebox.showinfo('วิธีคูณ','นี่คือตัวอย่าง 29 * 35= 1015')
def Divie():
	messagebox.showinfo('วิธีบวก','นี่คือตัวอย่าง 18 / 6 = 3')#(Date:8/3/2020)
######################Cricle#######################(Date:8/3/2020)
def Cricle(): #ถ้าฟังก์ชั้นใช้แล้วจบ ตัวแปรซ้ำได้ไม่มีผล ถ้าฟังก์ชั้นยังไม่จบ จะมีผล
	x = int(KK.get())
	sec = Pi * (x ** 2) #สามารถทำแบบนี้ได้เลย sec = 3.14 * (x ** 2) ไม่จำเป็นต้องไปแทนค่าเป็นค่า Pi หรือ ตัดวงเล็บไปก็ได้ผลลัพท์เดิม
	#sec = Pi * x ** 2 หรือแบบนี้ก็ได้ sec = 3.14 * x ** 2 [** คือ ยกกำลัง]
	result1.set(f'คำตอบคือ {sec:,.2f}') #:,.xf<--->x คือ จำนวนทศนิยม 
######################Funnel#######################(Date:8/12/2020 10:54 AM)
def Funnel():
	f = float(F.get())
	h = float(H.get())
	Ans = 1/3 * f *h
	SrFunnel.set(f'คำตอบคือ {Ans:,.2f}')
######################TA#########################
def TA():
	f = float(F.get())
	h = float(H.get())
	Ans = 1/2 * f * h
	Answer.set(f'คำตอบคือ: {Ans:,.2f}')
#################################################
def RbsF():
	fill_inB = float(Base_length.get())
	fill_inH = float(Height.get())
	Cal = fill_inB * fill_inH
	ResultRbs.set(f'Result is: {Cal:,.2f}')
#################################################
def RbsFV_2():
	Fill_inPODL = float(Product_of_diagonal_length.get())
	Cal1 = 1/2 * Fill_inPODL
	ResultRbs1.set(f'Result is: {Cal1:,.2f}')
#################################################
def CC():
	C = float(Cube.get())
	Ans = C**3
	CubeShowResalut.set(f'Answer is: {Ans:,.2f}')
#################################################
def CS():
	S = float(Spherical.get())
	Ans = 4/3*3.14*S**3
	SphericalShowResalut.set(f'Answer is: {Ans:,.2f}')
#################################################
def CCY():
	CYR = float(CylinderRadius.get())
	CYH = float(CylinderHight.get())
	Ans =(3.14*CYR**2)*CYH
	CylinderShowResalut.set(f'Answer is: {Ans:,.2f}')
#######################New File####################################
def New1File():
	GUI2 = Tk()
	GUI2.title('CalcurateProgram')
	GUI2.geometry('500x500')

	L1 = ttk.Label(GUI2,text='โปรแกรมคำนวณ[ผมคือแท็บใหม่]',font=FONT)
	L1.pack(pady=50)

	'''value1 = StringVar()
	value2 = StringVar()
	Result = StringVar()
	Result.set('-------')
	E1 = ttk.Entry(GUI2,textvariable=value1,font=FONT)
	E1.pack(ipadx=10,ipady=5)
	E2 = ttk.Entry(GUI2,textvariable=value2,font=FONT)
	E2.pack(ipadx=10,ipady=5,pady=50)
	B1 = ttk.Button(GUI2,text='คำนวณ',command=CalcuratE)
	B1.pack(ipadx=10,ipady=5)
	CResult = Label(GUI2,textvariable=Result)
	CResult.pack()'''

	GUI2.mainloop()
#######################New File#####################################(Date:8/3/2020)
GUI = Tk() #GUI เป็กการตั้งชื่อ เพื่อที่จะใช้ Tk()  

GUI.title('CalcurateProgram')
GUI.geometry('1000x500')


Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH)

F1 = Frame(Tab)
F2 = Frame(Tab)
F3 = Frame(Tab) #(Date:8/3/2020)
F4 = Frame(Tab)
F5 = Frame(Tab)
F6 = Frame(Tab)
F7 = Frame(Tab)
F8 = Frame(Tab)
F9 = Frame(Tab)

Tab.add(F1,text='พื้นฐานคำนวณ')
Tab.add(F2,text='วงกลม')
Tab.add(F3,text='กรวย') #(Date:8/3/2020)
Tab.add(F4,text='สามเหลี่ยม')
Tab.add(F5,text='สี่เหลี่ยมขนมเปียกปูน')
Tab.add(F6,text='สี่เหลี่ยมขนมเปียกปูนV_2')
Tab.add(F7,text='ลูกบาศก์')
Tab.add(F8,text='ทรงกลม')
Tab.add(F9,text='ทรงกระบอก')

menubar = Menu(GUI)
GUI.config(menu=menubar)

file = Menu(menubar,tearoff=0)
file.add_command(label='Close',command=GUI.quit)
file.add_command(label='New File',command=New1File)
menubar.add_cascade(label='File',menu=file)#สิ่งที่จะเอาไปวาง

calc = Menu(menubar,tearoff=0)
calc.add_command(label='การบวก',command=Plus)
calc.add_command(label='การลบ',command=Minus)
calc.add_command(label='การคูณ',command=Multiple)
calc.add_command(label='การหาร',command=Divie)
menubar.add_cascade(label='การคำนวณ',menu=calc)
#########################################################(Date:8/3/2020)
FONT = ('Angsana New',20)

L1 = ttk.Label(F1,text='โปรแกรมคำนวณ',font=FONT)#Lable ตัวหนังสือ
L1.pack(pady=50)

value1 = StringVar()
value2 = StringVar()
result = StringVar()
result.set('-------')

E1 = ttk.Entry(F1,textvariable=value1,font=FONT)
E1.pack(ipadx=10,ipady=5)

E2 = ttk.Entry(F1,textvariable=value2,font=FONT)
E2.pack(ipadx=10,ipady=5,pady=50)

B1 = ttk.Button(F1,text='คำนวณ',command=Calcurate)
B1.pack(ipadx=10,ipady=5)

LResult = Label(F1,textvariable=result)
LResult.pack()

######################F2#######################
L2 = ttk.Label(F2,text='โปรแกรมคำนวณ พท. วงกลม',font=FONT)#Lable ตัวหนังสือ
L2.pack(pady=50)

KK = StringVar()
Pi = float(3.14) #int ไม่นับทศนิยม ทำให้ค่า 3.14 จะโดนตัดไม่เอาไปคำนวณจะเหลือแค่ 3.00 ทำให้ค่าที่คำนวณมาผิดพลาด ถ้าจะคำนวณทศนิยมด้วยต้องใช้ float
result1 = StringVar()
result1.set('-------')

E5 = ttk.Entry(F2,textvariable=KK,font=FONT)
E5.pack(ipadx=10,ipady=5)

B2 = ttk.Button(F2,text='คำนวณ',command=Cricle)
B2.pack(ipadx=10,ipady=5)

RResult = Label(F2,textvariable=result1)
RResult.pack()
######################F3#######################
F = StringVar()
H = StringVar()
SrFunnel = StringVar()
SrFunnel.set('//////////////')

SrFunnelL1 = ttk.Label(F3,text='โปรแกรมคำนวณปริมาตรทรงกรวย',font=FONT)
SrFunnelL1.pack(pady=50)

SrFunnelE1 = ttk.Entry(F3,textvariable=F,font=FONT)
SrFunnelE1.pack(ipadx=10,ipady=5,padx=3,pady=3)

SrFunnelE2 = ttk.Entry(F3,textvariable=H,font=FONT)
SrFunnelE2.pack(ipadx=10,ipady=5,padx=3,pady=3)

SrFunnelB1 = ttk.Button(F3,text='คำนวณ',command=Funnel)
SrFunnelB1.pack(ipadx=10,ipady=5,padx=3,pady=3)

SwrFunnel = ttk.Label(F3,textvariable=SrFunnel,font=FONT)
SwrFunnel.pack()#Date(8/3/2020)
######################F4#######################
F = StringVar()
H = StringVar()
Answer = StringVar()
Answer.set('----------')

TAL1 = ttk.Label(F4,text='โปรแกรมคำนวณพื้นที่ สามเหลี่ยม',font=FONT)
TAL1.pack(pady=50)

TAE1 = ttk.Entry(F4,textvariable=F,font=FONT)
TAE1.pack(ipadx=10,ipady=5,padx=3,pady=3)

TAE2 = ttk.Entry(F4,textvariable=H,font=FONT)
TAE2.pack(ipadx=10,ipady=5,padx=3,pady=3)

TAB1 = ttk.Button(F4,text='คำนวณ',command=TA)
TAB1.pack(ipadx=10,ipady=5,padx=3,pady=3)

TAL2 = ttk.Label(F4,textvariable=Answer,font=FONT)
TAL2.pack()#Date
######################F5Variable###############
Base_length = StringVar()
Height = StringVar()
Product_of_diagonal_length = StringVar()
ResultRbs = StringVar()
ResultRbs.set('---------------')
ResultRbs1 = StringVar()
ResultRbs1.set('---------------')
###############################################
######################F5#######################
RbsLabel = ttk.Label(F5,text='โปรแกรมคำนวณ พท.สี่เหลี่ยมขนมเปียกปูน',font=FONT)
RbsLabel.pack()

RbsEntry = ttk.Entry(F5,textvariable=Base_length,font=FONT)
RbsEntry.pack()

RbsEntry1 = ttk.Entry(F5,textvariable=Height,font=FONT)
RbsEntry1.pack()

RbsButton = ttk.Button(F5,text='Calculate',command=RbsF)
RbsButton.pack()

RbsLabel1 = ttk.Label(F5,textvariable=ResultRbs,font=FONT)
RbsLabel1.pack()

######################F6#######################
RbsLabel2 = ttk.Label(F6,text='โปรแกรมคำนวณ พท.สี่เหลี่ยมขนมเปียกปูน',font=FONT)
RbsLabel2.pack()

RbsEntry2 = ttk.Entry(F6,textvariable=Product_of_diagonal_length,font=FONT)
RbsEntry2.pack()

RbsButton1 = ttk.Button(F6,text='Calculate',command=RbsFV_2)
RbsButton1.pack()

RbsLabel3 = ttk.Label(F6,textvariable=ResultRbs1,font=FONT)
RbsLabel3.pack()

#####################F7########################
Cube = StringVar()
CubeShowResalut = StringVar()
CubeShowResalut.set('----------')
########################
CubeLabel = ttk.Label(F7,text='Calculate of Cube')
CubeLabel.pack()

CubeEntry = ttk.Entry(F7,textvariable=Cube,font=FONT)
CubeEntry.pack()

CubeButton = ttk.Button(F7,text='Calculate',command=CC)
CubeButton.pack()

CubeLabel1 = ttk.Label(F7,textvariable=CubeShowResalut,font=FONT)
CubeLabel1.pack()
###############################################
Spherical = StringVar()
SphericalShowResalut = StringVar()
SphericalShowResalut.set('----------')
########################
SphericalLabel = ttk.Label(F8,text='Calculate of Spherical',font=FONT)
SphericalLabel.pack()

SphericalEntry = ttk.Entry(F8,textvariable=Spherical,font=FONT)
SphericalEntry.pack()

SphericalButton = ttk.Button(F8,text='Calculate',command=CS)
SphericalButton.pack()

SphericalLabel1 = ttk.Label(F8,textvariable=SphericalShowResalut,font=FONT)
SphericalLabel1.pack()
###############################################
CylinderRadius = StringVar()
CylinderHight = StringVar()
CylinderShowResalut = StringVar()
CylinderShowResalut.set('----------')
########################
CylinderLabel = ttk.Label(F9,text='Calculate of Cylinder',font=FONT)
CylinderLabel.pack()

CylinderEntry = ttk.Entry(F9,textvariable=CylinderRadius,font=FONT)
CylinderEntry.pack()

CylinderEntryH = ttk.Entry(F9,textvariable=CylinderHight,font=FONT)
CylinderEntryH.pack()

CylinderButton = ttk.Button(F9,text='Calculate',command=CCY)
CylinderButton.pack()

CylinderLabel1 = ttk.Label(F9,textvariable=CylinderShowResalut,font=FONT)
CylinderLabel1.pack()
###############################################
GUI.mainloop() #Last update 8/12/2020-10:58 AM
