def main():
    print("This is the main function.")

def hello(to = "world"):
    print("hello", to)

hello() # this will print hello world because we have provided a default value for the parameter to

name = input("Enter your name: ")
hello(name) # ask the user for the name and remove any leading or trailing whitespace and capitalize the first letter of the name

