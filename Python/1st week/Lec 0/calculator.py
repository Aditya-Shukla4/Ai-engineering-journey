# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))

def main():
    # x = int(input("Enter a number: "))
    # y = int(input("Enter another number: "))
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))

#! IN Documentation if we see [] these braces it genrally means that the parameter is optional and if we see {} these braces it generally means that the parameter is required and if we see () these braces it generally means that the parameter is a function or a method and if we see <> these braces it generally means that the parameter is a placeholder for a value that will be provided by the user or by the program at runtime.
z = round(x + y) # add the two numbers and store the result in z
# print(f"{z}")

#* If we want to add a comma btw number like as used for currecny what we can do is

print(f"{z:,}") # this will add a comma btw the number like as used for currecny