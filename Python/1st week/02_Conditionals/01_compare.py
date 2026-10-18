x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x > y:
    #! In python we don't have curly braces, we use indentation to define blocks of code
    # If we use only if no matter what the condition is, it will always check the next condition, so we use elif to avoid that
    print(f"{x} is greater than {y}")
#* We can use elif this is the version of else if in python 
# we use elif to check another condition if the first one is false
elif x < y:
    print(f"{x} is less than {y}")
# we can use else to catch all the other cases, in this case if x is equal to y
else:
    print(f"{x} is equal to {y}")