import math

print("Scientific Calculator")
print("Operations: power, sqrt, sin, cos, tan, log")

op = input("Enter operation: ")

if op == 'p':
    base = float(input("Enter base: "))
    exp = float(input("Enter exponent: "))
    result = math.pow(base, exp) # power for 2^3=8 base is 2 exp is 3

elif op == "sqrt":
    num = float(input("Enter number: "))
    if num < 0:
        result = "Error: Cannot find square root of negative number"
    else:
        result = math.sqrt(num) # square root
#  python expect RADIANS not degree so 1st convert to degree
elif op == "sin":
    angle = float(input("Enter angle in degrees: "))
    result = math.sin(math.radians(angle))   #convert degree to radian

elif op == "cos":
    angle = float(input("Enter angle in degrees: "))
    result = math.cos(math.radians(angle))

elif op == "tan":
    angle = float(input("Enter angle in degrees: "))
    result = math.tan(math.radians(angle))

elif op == "log":
    num = float(input("Enter number: "))
    base = float(input("Enter base (press 10 for common log, 2.718 for natural log): "))
    result = math.log(num, base)  # log 20

else:
    result = "Error: Invalid operation"

print("Result:", result)