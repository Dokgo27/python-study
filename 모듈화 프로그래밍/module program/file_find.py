# 20192827 김민재

password = open("C:/Users/J/OneDrive/대학/2022 1학기/프기/6강 실습/임의 프로그램/password.txt")

def find_password(year, month, day, time):

    for line in password:
        s = {}
        (s["year"], s["month"], s["day"], s["time"], s["password"], s["school number"], s["name"]) = line.split("/")


        if (year == int(s["year"])):
            if(month == int(s["month"])):
                if(day == int(s["day"])):
                    if(time == int(s["time"])):
                        return (s)
        else:
            return ({})
         

input_year = int(input("\nyear? <please input (0000)>: "))

input_month = int(input("month? <please input (00)>: "))

input_day = int(input("day? <please input (00)>: "))

input_time = int(input("time? <please input (00)>: "))

a = input_year
b = input_month
c = input_day
d = input_time

password_line = find_password(a, b, c, d)
    
if password_line:
    print("\nyear:             " + password_line["year"])
    print("month:            " + password_line["month"])
    print("day:              " + password_line["day"])
    print("time:             " + password_line["time"])
    print("password:         " + password_line["password"])
    print("school number:    " + password_line["school number"])
    print("name:             " + password_line["name"])


    