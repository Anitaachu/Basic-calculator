"""This is a basic calculator project"""

num1 = float(input("Enter number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter number: "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Incorrect operator!")
