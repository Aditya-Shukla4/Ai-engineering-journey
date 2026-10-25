# This is a function that prompts the user to enter a number and handles exceptions for invalid input.
def main():
    number = get_int()
    print(f"You entered: {number}")

def get_int():
    # Using loop so that we can keep asking for input until a valid integer is provided
    while True:
        # try block to catch ValueError if the input is not an integer
        try:
            number = int(input("Enter a number: "))
            # If the conversion is successful, we break out of the loop and return the number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        # If an exception is caught, we continue the loop and ask for input again
        else:
            return number

main()

#these were a way there is another statment that is pass we shoukld read about it and understand it
#that is if we use pass we don't print a msg to the user it just catches the error and continues the loop without any feedback to the user.