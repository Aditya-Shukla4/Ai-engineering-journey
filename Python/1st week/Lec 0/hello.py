# First program in python
name = input("Enter your name: ")

# as mentioned below jaise end hai waise hi ek or parameter hai jo ki hai sep = " " iski wajah se hum kya karenge ki hum name ke bich me space de denge wo already ek space deta hai by default hum uski value bhi chhed skte hai
print("hello." , end = "")
# IF we use this isme wo agli line pe leke chala jata hai usme 
# "/n" already laga hua hai usi wajah se phir ab hum kya kreege ki  uski documentation me dekha ki print() function me end parameter hota hai jisme end = "\n" hai hai jiski wajah se ye agle line pe chala jata hai to hum kya karenge ki end = " " kar denge to ye agle line pe nahi jayega aur hum uske baad name print kar denge
# print(name)
# what we can do is to pass the paramter or print the name like

# print(f"hello {name}") # we shouldn't use this very often but it is just another way of doing it

#! what if we want to write double quotes inside double quotes then we can use it in multiple ways

# print("hello \"world\"") # we can use backslash to escape the double quotes the backslash will tell the compiler that this is not the end of the string but it is a part of the string it is called the escape character
#* Or we can use single quotes to weite double quotes inside double quotes
# print('hello "world"') # we can use single quotes to write double quotes inside doublequotes something like this


