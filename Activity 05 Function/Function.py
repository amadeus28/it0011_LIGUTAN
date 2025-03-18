def divide(a, b):
    if b == 0:
        print("Error: The second number or denominator must not be equal to zero.")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: The second number or denominator must not be equal to zero.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Error: The second number must be greater than the first number.")
        return None
    
    a = int(a)
    b = int(b)
    total = 0
    
    for i in range(a, b + 1):
        total += i
    return total

def main():
    while True:
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter the letter of choice: ").upper()
        
        if choice == 'D' or choice == 'E' or choice == 'R' or choice == 'F':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if choice == 'D':
                result = divide(a, b)
            elif choice == 'E':
                result = exponentiation(a, b)
            elif choice == 'R':
                result = remainder(a, b)
            elif choice == 'F':
                result = summation(a, b)
            
            if result is not None:
                print("Result:", result)
                
        elif choice == 'Q':
            break
        else:
            print("Invalid choice. Please try again.")

main()