#1.ADD
#2.SUBTRACT
#3.MULTIPLY
#4.DIVISION
operator=input("Enter an operator(+ - * /):")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if operator=="+":
    print("sum is:"+str((num1)+(num2)))
elif operator=="-":
    print("subtraction is:"+str((num1)-(num2)))
elif operator=="*":
    print("multiplication is:"+str((num1)*(num2)))
elif operator=="/":
    print("Division is:"+str((num1)/(num2)))
else:
    print("Invalid input")