def calculator():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the mathematical operation you want(add,subtract,multiply,divide): ")

    if operation == "add":
        print(a+b)
    elif operation == "subtract":
        print(a-b)
    elif operation == "multiply":
        print(a*b)
    elif operation == "divide":
        print(a%b)
        if b == 0:
            print("You can't divide by zero")
    else:
        print("invalid operation")

calculator()



 
