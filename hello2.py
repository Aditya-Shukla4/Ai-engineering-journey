#ask the user for the name
name = input("Enter your name: ").strip().title()
#we can add all of this in a single line it is all arguable obviously but it is a good practice to do it in a single line because it is more readable and it is more efficient because we are not creating multiple variables and we are not using multiple lines of code to do the same thing

# name = name.strip() # remove any leading or trailing whitespace from the name

# name = name.capitalize() # capitalize the first letter of the name
first , last = name.split(" ") # split the name into first and last name

print(f"hello , {first}") # print the first 

