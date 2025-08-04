#Calc Program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")


if operation == '+':
    sum_result = num1 + num2
    print(f"sum: {sum_result}")
elif operation == '-':
    difference_result = num1 - num2
    print(f"difference: {difference_result}")
elif operation == '*':
    Product_result = num1 * num2
    print(f"Product: {Product_result}")
elif operation == '/':
    if num2 != 0:
        Quotient_result = num1 / num2
        print(f"Quotient: {Quotient_result}")
    else:
        print("Invalid operation. Enter operations below +, -, *, or /.")
else:
    print("Error")
