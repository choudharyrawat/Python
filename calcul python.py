import math
def welcome():
    print('''Welcome to Calculator''')

welcome()
print(""" 
press -  
1- Addition(x, y) 
2- Subtraction(x,y) 
3- Multiplication(x,y) 
4- Division(x, y) 
5- Exponent(x, y) 
6 - Tan(x, y) 
7 - Sin(x) 
8 - Cos(x) 
9-Mod(%)
10-Square root
11-Degree to Radian
12-Radian to Degree
""")
def calculate():
    
    o = input("Select: ")
    if o == "1":
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("Sum: ",x + y)
    elif o == "2":
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("Subtract: ",x-y)
    elif o == "3":
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("Multiply: ",x*y)
    elif o == "4":
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("Divide: ",x/y)
    elif o == "5":
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("Exponent: ",x**y)
    elif o == "6":
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("Tan value: ",math.tan(x))
    elif o == "7":
        x = float(input("Enter Number: "))
        print("Sin value: ",math.sin(x))
    elif o == "8":
        x = float(input("Enter Number: "))
        print("Cos value: ",math.cos(x))
    elif o == "9":
        x = float(input("Enter Number: "))
        y = float(input("Enter Number: "))
        print("Modulus: ",x%y)
    elif o == "10":
        x = float(input("Enter Number: "))
        print("Square root: ",math.sqrt(x))
    elif o == "11":
        x = float(input("Enter Number: "))
        print("Degree to Radian: ",math.radians(x))
    elif o == "12":
        x = float(input("Enter Number: "))
        print("Radian to Degree: ",math.degrees(x))
    else:
        print('You have not typed a valid option, please run the program again.')

    again()
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
calculate()
