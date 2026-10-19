text = input("File name:")

if text.lower().endswith(".gif"):
    print("image/gif")
elif text.lower().endswith(".jpg") or text.lower().endswith(".jpeg"):
    print("image/jpeg")
elif text.lower().endswith(".png"):
    print("image/png")
elif text.lower().endswith(".pdf"):
    print("application/pdf")
elif text.lower().endswith(".txt"):
    print("text/plain")
elif text.lower().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")