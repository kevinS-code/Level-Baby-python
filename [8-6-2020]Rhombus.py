#Rhombus.py
from tkinter import *
from tkinter import ttk

############Screen##############
Rbs = Tk()
Rbs.geometry('500x500')
Rbs.title('โปรแกรมคำนวณ พท.สี่เหลี่ยมขนมเปียกปูน')
Tab = ttk.Notebook(Rbs)
Tab.pack(fill=BOTH)
Rbs = Frame(Tab)#Frame1
Rbs1 = Frame(Tab)#Frame2
Tab.add(Rbs,text='Rbs')
Tab.add(Rbs1,text='V_2')

################################
############Function############
def RbsF():
	fill_inB = float(Base_length.get())
	fill_inH = float(Height.get())
	Cal = fill_inB * fill_inH
	ResultRbs.set(f'Result is: {Cal:,.2f}')

def RbsFV_2():
	Fill_inPODL = float(Product_of_diagonal_length.get())
	Cal1 = 1/2 * Fill_inPODL
	ResultRbs1.set(f'Result is: {Cal1:,.2f}')

################################
############Variable############
FONT = ('Angsana New',20)
Base_length = StringVar()
Height = StringVar()
Product_of_diagonal_length = StringVar()
ResultRbs = StringVar()
ResultRbs.set('---------------')
ResultRbs1 = StringVar()
ResultRbs1.set('---------------')

################################
###########Widget Rbs###########
RbsLabel = ttk.Label(Rbs,text='โปรแกรมคำนวณ พท.สี่เหลี่ยมขนมเปียกปูน',font=FONT)
RbsLabel.pack()

RbsEntry = ttk.Entry(Rbs,textvariable=Base_length,font=FONT)
RbsEntry.pack()

RbsEntry1 = ttk.Entry(Rbs,textvariable=Height,font=FONT)
RbsEntry1.pack()

RbsButton = ttk.Button(Rbs,text='Calculate',command=RbsF)
RbsButton.pack()

RbsLabel1 = ttk.Label(Rbs,textvariable=ResultRbs,font=FONT)
RbsLabel1.pack()

###########Widget Rbs1############
RbsLabel2 = ttk.Label(Rbs1,text='โปรแกรมคำนวณ พท.สี่เหลี่ยมขนมเปียกปูน',font=FONT)
RbsLabel2.pack()

RbsEntry2 = ttk.Entry(Rbs1,textvariable=Product_of_diagonal_length,font=FONT)
RbsEntry2.pack()

RbsButton1 = ttk.Button(Rbs1,text='Calculate',command=RbsFV_2)
RbsButton1.pack()

RbsLabel3 = ttk.Label(Rbs1,textvariable=ResultRbs1,font=FONT)
RbsLabel3.pack()

################################

Rbs.mainloop()
