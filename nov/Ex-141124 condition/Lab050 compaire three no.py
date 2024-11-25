num1=float(input('"Enter your fist no:'))
num2=float(input('"Enter your Second no:'))
num3=float(input('"Enter your Third no:'))
if num1>=num2 and num1>=num3:
    print("max no is ",num1)
elif num2>=num1 and num2>=num3:
    print("max no is",num2)
else:
    print("max no is",num3)