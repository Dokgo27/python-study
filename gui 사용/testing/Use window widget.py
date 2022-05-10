# 20192827 김민재

from tkinter import *

password = open("C:/Users/J/OneDrive/대학/2022 1학기/프기/6강 실습/임의 프로그램/password.txt")

def find_password(year, month, day, time):

    for line in password:
        s = {}
        (s["year"], s["month"], s["day"], s["time"], s["password"], s["school number"], s["name"]) = line.split("/")


        if (year == int(s["year"])):
            if(month == int(s["month"])):
                if(day == int(s["day"])):
                    if(time == int(s["time"])):
                        if s:
                            print("\nyear:             " + s["year"])
                            print("month:            " + s["month"])
                            print("day:              " + s["day"])
                            print("time:             " + s["time"])
                            print("password:         " + s["password"])
                            print("school number:    " + s["school number"])
                            print("name:             " + s["name"])
                        return (s)
        else:
            return ({})

def password_find():
    a = 0
    b = 0
    c = 0
    d = 0

    a = Text_input1.get()
    b = Text_input2.get()
    c = Text_input3.get()
    d = Text_input4.get()

    a1 = int(a)
    b1 = int(b)
    c1 = int(c)
    d1 = int(d)
 
    find_password(a1, b1, c1, d1)
    return

app = Tk()
app.geometry("300x200+200+100")

## section 1
lab1 = Label(app, text= "year? <please input (0000)>: ")
lab1.pack()
Text_input1 = Entry(app)
Text_input1.pack()

## section 2
lab2 = Label(app, text= "month? <please input (00)>: ")
lab2.pack()
Text_input2 = Entry(app)
Text_input2.pack()

## section 3
lab3 = Label(app, text= "day? <please input (00)>: ")
lab3.pack()
Text_input3 = Entry(app)
Text_input3.pack()

## section 4
lab4 = Label(app, text= "time? <please input (00)>:")
lab4.pack()
Text_input4 = Entry(app)
Text_input4.pack()

## button
button1 = Button(app, text="find", command = password_find)
button1.pack()

app.mainloop()






    