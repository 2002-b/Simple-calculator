def add(a,b):
    result = a+b
    print(result)

def sub(a,b):
    result = a-b
    print(result)

def mul(a,b):
    result = a*b
    print(result)

def div(a,b):
    result = a/b
    print(result)

a = int(input('enter the first number:'))
b = int(input('enter the second number:'))
op=input("enter the operator:")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("invalid operator:")
