while True:
    try:
        #This is where user will input a number and symbol 
        First_n = float(input("Enter a number (or 'q' to quit): "))
        #If the user inputs 'q' the program will break and end
        if isinstance(First_n, str) and First_n.lower() == 'q':
            break
        symbol = input("Enter a symbol (+, -, *, /, ^^): ")
        Second_n = float(input("Enter another number: "))
        
        #This is where the program will calculate the numbers and symbol
        if symbol == "+":
            result = First_n + Second_n
        elif symbol == "-":
            result = First_n - Second_n
        elif symbol == "*": 
            result = First_n * Second_n
        elif symbol == "/":
            if Second_n != 0:
                result = First_n / Second_n
            else:
                print("Error: Division by zero")
                continue
        elif symbol == "^^": 
            result = First_n ** Second_n
        
        else:
            print("Invalid symbol")
            continue
        #This is where the program will print the result
        print(f"Result: {result}")
    #This is where the program will catch any errors
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    print("\n--- New Calculation ---\n")

print("Calculator closed. Goodbye!")