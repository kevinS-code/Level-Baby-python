#Parallelogram.py
from tkinter import *
from tkinter import ttk

############Screen##############
Par = Tk()
Par.geometry('500x500')
Par.title('โปรแกรมคำนวณ พท.สี่เหลี่ยมด้านขนาน')

################################
############Function############
def ParF():
	fill_inB = float(Base.get())
	fill_inH = float(Height.get())
	Cal = fill_inB * fill_inH
	ResultPar.set(f'Result is: {Cal:,.2f}')

################################
############Variable############
FONT = ('Angsana New',20)
Base = StringVar()
Height = StringVar()
ResultPar = StringVar()
ResultPar.set('---------------')

################################
###########Widget Par###########
ParLabel = ttk.Label(Par,text='โปรแกรมคำนวณ พท.สี่เหลี่ยมด้านขนาน',font=FONT)
ParLabel.pack()

ParEntry = ttk.Entry(Par,textvariable=Base,font=FONT)
ParEntry.pack()

ParEntry1 = ttk.Entry(Par,textvariable=Height,font=FONT)
ParEntry1.pack()

ParButton = ttk.Button(Par,text='Calculate',command=ParF)
ParButton.pack()

ParLabel1 = ttk.Label(Par,textvariable=ResultPar,font=FONT)
ParLabel1.pack()

################################

Par.mainloop() #Check 8/7/2020-8:59 PM