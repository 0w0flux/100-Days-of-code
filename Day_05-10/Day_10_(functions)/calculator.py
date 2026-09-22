import art


def plus(num1, num2):
    return num1 + num2

def minus(num1, num2): 
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

def main(calc_final=False, previous_answer=None):

    # skips the first input if the user wants to continue calculating with the previous answer
    if calc_final and previous_answer is not None: 
        num1 = previous_answer
    else:
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input!")

    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ["+", "-", "*", "/"]:
            break
        print("Invalid input!")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input!")

    if operation == "+":
        answer = plus(num1, num2)
    elif operation == "-":
        answer = minus(num1, num2)
    elif operation == "*":
        answer = multiply(num1, num2)
    elif operation == "/":
        answer = divide(num1, num2)

    result = f"{num1} {operation} {num2} = {answer}"
    print(result)

    while True:
        calculate_again = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
        # either goes back to the old answers or quits the program
        if calculate_again == "q": 
            break
        elif calculate_again == "y":
            main(calc_final=True, previous_answer=answer)
        elif calculate_again == "n":
            main()
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

if __name__ == "__main__":
    print(art.logo)
    main()
