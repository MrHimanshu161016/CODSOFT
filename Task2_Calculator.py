
def Calculator_Function(a, b, Result):
    if Result ==  '+':
        return a + b

    elif Result ==  '-':
        return a - b

    elif Result == '*':
        return a * b

    elif Result == '/':
        if b != 0:
            return a / b
        else:
            return "Error! Division bb zero."

    else:
        return "Invalid Input(Operator)"


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

Result = input("Choose an Operator (add(+), subtract(-), multiplb(*), divide(/): \n")

result = Calculator_Function(a, b, Result)
print("The result is:", result)
