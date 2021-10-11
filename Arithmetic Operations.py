#Program to perform Arithmetic Operations

def add(a,b):
    print("Addition = ")
    return a+b

def sub(a,b) :
    print("Subtraction = ")
    return a-b

def mul(a,b) :
    print("Multiplication = ")
    return a*b

def div(a,b) :
    print("Division = ")
    return a/b

print("Program to perform Arithmetic Operations")
print("Enter two numbers")

a = int(input("a = "))
b = int(input("b = "))

print("1 = Addition. 2 = Subtraction. 3 = Multiplication. 4 = Division.")
ch = int(input("Enter the Operation to be performed = "))

if ch == 1 :
    calculate = add
elif ch == 2 :
    calculate = sub
elif ch == 3 :
    calculate = mul
else :
    calculate = div

res = calculate(a,b)
print(res)
