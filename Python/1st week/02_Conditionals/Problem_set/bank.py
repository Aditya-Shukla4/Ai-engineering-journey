text = input("Greeting: ")

if text.lower().startswith("hello"):
    print("$0")

elif text.lower().startswith("h"):
    print("$20")

else:
    print("$100")