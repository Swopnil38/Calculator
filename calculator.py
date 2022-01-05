from tkinter import*
window = Tk()
window.geometry("240x220")

value = Entry(window,width=35)
value.grid(row=0,column = 0,columnspan=4,padx=10,pady=10)

def button_click(num):
    current = value.get()
    expression = str(current)+str(num)
    value.delete(0,END)
    value.insert(0,expression)

def button_equal():
    number = value.get()
    total = str(eval(number))
    value.delete(0,END)
    value.insert(0,total)

def button_clear():
    value.delete(0,END)

num_9 = Button(window,text="9",padx= 20,pady=10,command=lambda : button_click(9)).grid(row=1,column=3)
num_8 = Button(window,text="8",padx= 20,pady=10,command=lambda : button_click(8)).grid(row=1,column=2)
num_7 = Button(window,text="7",padx= 20,pady=10,command=lambda : button_click(7)).grid(row=1,column=1)
num_plus = Button(window,text="+",padx= 20,pady=10,command=lambda : button_click("+")).grid(row=1,column=0)
num_6 = Button(window,text="6",padx= 20,pady=10,command=lambda : button_click(6)).grid(row=2,column=3)
num_5 = Button(window,text="5",padx= 20,pady=10,command=lambda : button_click(5)).grid(row=2,column=2)
num_4 = Button(window,text="4",padx= 20,pady=10,command=lambda : button_click(4)).grid(row=2,column=1)
num_sub = Button(window,text="-",padx= 20,pady=10,command=lambda : button_click("-")).grid(row=2,column=0)
num_3 = Button(window,text="3",padx= 20,pady=10,command=lambda : button_click(3)).grid(row=3,column=3)
num_2 = Button(window,text="2",padx= 20,pady=10,command=lambda : button_click(2)).grid(row=3,column=2)
num_1 = Button(window,text="1",padx= 20,pady=10,command=lambda : button_click(1)).grid(row=3,column=1)
num_mul = Button(window,text="*",padx= 20,pady=10,command=lambda : button_click("*")).grid(row=3,column=0)
num_div = Button(window,text="/",padx= 20,pady=10,command=lambda : button_click("/")).grid(row=4,column=3)
num_equal = Button(window,text="=",padx= 20,pady=10,command=button_equal).grid(row=4,column=2)
num_clear = Button(window,text="Clear",padx= 10,pady=10,command=button_clear).grid(row=4,column=1)
num_0 = Button(window,text="0",padx= 20,pady=10,command=lambda : button_click(0)).grid(row=4,column=0)


window.mainloop()
