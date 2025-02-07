number = input("Please enter a number: ")

number = number.strip()

if number.isdigit() or (number[0] == '-' and number[1:].isdigit()):
    num_digits = len(number) if number[0] != '-' else len(number) - 1
    print(f"The number of digits in {number} is: {num_digits}")
else:
    print("Invalid input. Please enter a valid integer.")