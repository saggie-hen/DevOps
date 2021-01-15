import random

def e1():
    first = 7
    second = 44.3
    print(first + second)
    print(first * second)
    print(second / first)

def e2():
    a = 8
    a = 17
    a = 9
    b = 6
    c = a + b
    b = c + a
    b = 8
    print(f'a: {a}, b: {b}, c: {c}')

def e3():
    name1 = "john"
    name2 = 'john'
    if(name1 == name2):
        print("Both are string")

    my_number = 5 + 5
    print("result is: " + str(my_number))
    print(f"result is: {my_number}")

def e4():
    x = 5
    y = 2.36
    print(x+int(y))

def e5(x,y):
    if(x > y):
        print("BIG")
    elif(x < y):
        print("Small")
    else:
        print("Equal")

def e6():
    number = random.randint(1,4)
    if(number == 1):
        print("Summer")
    elif(number == 2):
        print("Winter")
    elif(number == 3):
        print("Fall")
    elif(number == 4):
        print("Spring")

def e7():
    a = 8
    b = "123"
    print(a + int(b))
# extra
def extra1():
    var1 = "5"
    var2 = 5
    comp = var1 == var2
    sum = int(var1) + var2
    print(f"{comp},{sum}")
    if(5 > 5.5):
        print("5 is bigger than 5.5")
    if(True == False):
        print("True")
    else:
        print("False")

def larger(a,b):
    if(len(a) > len(b)):
        print("a is larger, Len: " + str(len(a)))
    elif(len(b) > len(a)):
        print("b is larger, Len: " + str(len(a)))
def extra2():
    while True:
        name = input("enter your name")
        if(name[0] == 'A'):
            print("starts with 'A'")
            break
        else:
            print("your name must stats with 'A'")
            continue
    age = input("enter your age")
    if(isinstance(age, int) == False):
        print("age is not Int, " + str(type(age)))
    else:
        print("age is Int")
    work = input("enter your work")

    print(f"Name: {name}, Age: {age}, Work: {work}")

e1()
e2()
e3()
e4()
e5(1,3)
e5(3,1)
e5(2,2)
e6()
e7()
extra1()
larger("hello","helloo")
extra2()