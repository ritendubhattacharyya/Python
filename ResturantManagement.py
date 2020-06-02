from tkinter import *
from tkinter import messagebox
import random

# start coding

# global variables

calculator_entry=""
sum = 0

# Commands


def getNumber(number):
    global calculator_entry
    calculator_entry = calculator_entry + number
    calc_entry.delete(0, END)
    calc_entry.insert(0, calculator_entry)


def clear_element():
    global calculator_entry
    temp_list = list(calculator_entry)
    temp_list.pop()
    calculator_entry = "".join(temp_list)
    calc_entry.delete(0, END)
    calc_entry.insert(0, calculator_entry)


def clear_all():
    global calculator_entry
    calc_entry.delete(0, END)
    calculator_entry=""


def equal():
    try:
        result = eval(calc_entry.get())
        calc_entry.delete(0, END)
        calc_entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Wrong Input", e)


def calculate():
    global sum
    try:
        total_entry.delete(0, END)
        service_tax_entry.delete(0, END)
        gst_entry.delete(0, END)
        grand_total_entry.delete(0, END)
        random_entry.delete(0, END)
        coffee_price = 0 if (coffee_entry.get() == "") else(int(coffee_entry.get())*50)
        tea_price = 0 if(tea_entry.get() == "") else(int(tea_entry.get())*10)
        biriyani_price = 0 if(biriyani_entry.get() == "") else(int(biriyani_entry.get())*170)
        chicken_price = 0 if(chicken_entry.get() == "") else(int(chicken_entry.get())*100)
        cold_drinks_price = 0 if(cold_drinks_entry.get() == "") else(int(cold_drinks_entry.get())*40)
        if(coffee_price==0 and tea_price==0 and biriyani_price==0 and chicken_price==0 and cold_drinks_price==0):
            return
        sum = coffee_price + tea_price + biriyani_price + chicken_price + cold_drinks_price
        service_tax = sum * (4/100)
        gst = sum * (18/100)
        grand_total = sum + service_tax + gst
        total_entry.insert(0, sum)
        service_tax_entry.insert(0, service_tax)
        gst_entry.insert(0, gst)
        grand_total_entry.insert(0, grand_total)
        sum = 0
        random_entry.insert(0, str(random.randrange(1, 8000)))
    except Exception as e:
        messagebox.showerror("Wrong Input", e)

        

def reset():
    coffee_entry.delete(0, END)
    tea_entry.delete(0, END)
    biriyani_entry.delete(0, END)
    chicken_entry.delete(0, END)
    cold_drinks_entry.delete(0, END)
    total_entry.delete(0, END)
    service_tax_entry.delete(0, END)
    gst_entry.delete(0, END)
    grand_total_entry.delete(0, END)
    random_entry.delete(0, END)


# Design
root = Tk()
root.geometry("1200x600")
root.title("Resturant Management")
root.configure(background="#32a852")
#============================================TITLE================================================================
frame_title = LabelFrame(root, bg="#32a852")
frame_title.pack(side=TOP)
Title = Label(frame_title, text="RESTURANT MANAGEMENT SYSTEM", pady=20, font=("arial", 47, "bold"), bg="#32a852", fg="#ffffff")
Title.pack()
#============================================Calc==================================================================
frame_calc = LabelFrame(root, bg="#32a852")
frame_calc.pack(side=RIGHT)
calc_entry = Entry(frame_calc,
                   bg="#dbffe5",
                   fg="#000000",
                   bd=3,
                   justify="right",
                   width=50,
                   cursor="dot",
                   borderwidth=10)
calc_entry.grid(row=0, column=0, columnspan =4)

button_7 = Button(frame_calc,
                  text="7",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("7")).grid(row=1, column=0)
button_8 = Button(frame_calc,
                  text="8",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  command=lambda:getNumber("8"),
                  relief=RAISED).grid(row=1, column=1)
button_9 = Button(frame_calc,
                  text="9",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("9")).grid(row=1, column=2)
button_devide = Button(frame_calc,
                  text="/",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("/")).grid(row=1, column=3)

button_4 = Button(frame_calc,
                  text="4",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("4")).grid(row=2, column=0)
button_5 = Button(frame_calc,
                  text="5",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("5")).grid(row=2, column=1)
button_6 = Button(frame_calc,
                  text="6",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("6")).grid(row=2, column=2)
button_multiply = Button(frame_calc,
                  text="X",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("*")).grid(row=2, column=3)

button_1 = Button(frame_calc,
                  text="1",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("1")).grid(row=3, column=0)
button_2 = Button(frame_calc,
                  text="2",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("2")).grid(row=3, column=1)
button_3 = Button(frame_calc,
                  text="3",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("3")).grid(row=3, column=2)
button_minus = Button(frame_calc,
                  text="-",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("-")).grid(row=3, column=3)

button_point = Button(frame_calc,
                  text=".",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber(".")).grid(row=4, column=0)
button_0 = Button(frame_calc,
                  text="0",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("0")).grid(row=4, column=1)
button_CE = Button(frame_calc,
                  text="E",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=clear_element).grid(row=4, column=2)
button_plus = Button(frame_calc,
                  text="+",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("+")).grid(row=4, column=3)

button_openBracket = Button(frame_calc,
                  text="(",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber("(")).grid(row=5, column=0)
button_closeBracket = Button(frame_calc,
                  text=")",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=lambda:getNumber(")")).grid(row=5, column=1)
button_C = Button(frame_calc,
                  text="C",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=clear_all).grid(row=5, column=2)
button_equal = Button(frame_calc,
                  text="=",
                  padx=33,
                  pady=30,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=equal).grid(row=5, column=3)
#============================================Item Selection========================================================
frame_item = LabelFrame(root, bg="#32a852", padx=20)
frame_item.pack(side=LEFT)
# row0
random_label = Label(frame_item,
                    text="Random id",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=0, column=0, padx=7, pady=7)

random_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
random_entry.grid(row=0, column=1, padx=7, pady=7)

Total_label = Label(frame_item,
                    text="Total",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=0, column=2, padx=7, pady=7)

total_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
total_entry.grid(row=0, column=3, padx=7, pady=7)

# row1
coffee_label = Label(frame_item,
                    text="Coffee",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=1, column=0, padx=7, pady=7)

coffee_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
coffee_entry.grid(row=1, column=1, padx=7, pady=7)

service_tax_label = Label(frame_item,
                    text="Service Tax",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=1, column=2, padx=7, pady=7)

service_tax_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
service_tax_entry.grid(row=1, column=3, padx=7, pady=7)
#row2
tea_label = Label(frame_item,
                    text="Tea",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=2, column=0, padx=7, pady=7)

tea_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
tea_entry.grid(row=2, column=1, padx=7, pady=7)

gst_label = Label(frame_item,
                    text="GST",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=2, column=2, padx=7, pady=7)

gst_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
gst_entry.grid(row=2, column=3, padx=7, pady=7)
# row3
biriyani_label = Label(frame_item,
                    text="Biriyani",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=3, column=0, padx=7, pady=7)

biriyani_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
biriyani_entry.grid(row=3, column=1, padx=7, pady=7)

grand_total_label = Label(frame_item,
                    text="Grand Total",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=3, column=2, padx=7, pady=7)

grand_total_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
grand_total_entry.grid(row=3, column=3, padx=7, pady=7)
# row4
chicken_label = Label(frame_item,
                    text="Chicken",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=4, column=0, padx=7, pady=7)

chicken_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
chicken_entry.grid(row=4, column=1, padx=7, pady=7)
# row5
cold_drinks_label = Label(frame_item,
                    text="Cold Drinks",
                    fg="#ffffff",
                    bg="#32a852",
                    font=("arial", 10)).grid(row=5, column=0, padx=7, pady=7)

cold_drinks_entry = Entry(frame_item,
                    bg="#dbffe5",
                    fg="#000000",
                    width=30,
                    bd=3,
                    justify="right",
                    cursor="arrow",
                    borderwidth=6)
cold_drinks_entry.grid(row=5, column=1, padx=7, pady=7)
# row6

button_total = Button(frame_item,
                  text="TOTAL",
                  font=("arial",10,"bold"),
                  padx=40,
                  pady=17,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=calculate).grid(row=6, column=1)
button_reset = Button(frame_item,
                  text="RESET",
                  font=("arial",10,"bold"),
                  padx=40,
                  pady=17,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=reset).grid(row=6, column=2)
button_exit = Button(frame_item,
                  text="EXIT",
                  font=("arial",10,"bold"),
                  padx=40,
                  pady=17,
                  bg="#9cffcd",
                  fg="#000000",
                  relief=RAISED,
                  command=root.destroy).grid(row=6, column=3)




#============================================End_Root==============================================================
root.mainloop()
