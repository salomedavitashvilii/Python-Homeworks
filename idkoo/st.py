def calculator():
    nums = input("Enter what you want to calculate: ")
    data = nums.split()
    
    if len(data) != 3:
        return "Invalid input. Please provide an expression with two numbers and an operator."
    
    num1 = float(data[0])
    operator = data[1]
    num2 = float(data[2])

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Invalid input. You cannot divide a number by zero."
        else:
            return num1 / num2
    elif operator == "^":
        return num1 ** num2
    else:
        return "Invalid input. Please enter a valid operator: '+', '-', '*', '/', '^'."
print(calculator())

