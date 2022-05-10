import random

def Wantpassword():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    special = "!@#$%^&*?"
    password = ""
 
    nu = input("몇자리의 숫자를 원하십니까?: ")
    num =  int(nu)
    
    ap = input("몇자리의 알파벳을 원하십니까?: ")
    apa = int(ap)

    sp = input("몇자리의 특수문자을 원하십니까?: ")
    spe = int(sp)

    for i in range(num):
        index_n = random.randrange(len(number))
        password = password + number[index_n]
 
    for i in range(apa):
        index_a = random.randrange(len(alphabet))
        password = password + alphabet[index_a]

    for i in range(spe):
        index_s = random.randrange(len(special))
        password = password + special[index_s]
    return password