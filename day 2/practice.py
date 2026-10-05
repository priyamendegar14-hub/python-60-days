#positive/negative
num=int(input("enter your number:"))
if num>0:
    print("positive")
else:
    print("negative")    


#even/odd
number=int(input("enter your number:"))
if number % 2 == 0:
    print("even")
else:
    print("odd")    



#largrst of two numbers 
a=int(input("enter your first number:"))
b=int(input("enter your second number"))
if a>=b:
    print("a is larger")
else:
    print("b is larger")    


#grade calculator
marks=int(input("enter your marks:"))
if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
else:
    print("fail")


#ATM withdrawal 
balance=float(input("enter your balance:"))
amount=float(input("enter withdrawal amount:"))
if amount < 0:
    print("invalid withdrawal amount")
elif amount > balance:
    print("insufficient balance:")
else:
    print("withdrawal successful")
    print("remaining balance:", balance-amount)