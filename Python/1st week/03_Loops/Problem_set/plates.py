def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False
#Using Flag here
    number_started = False

    for c in s:
        if not c.isalnum():
            return False 

        if c.isalpha() and number_started:
            return False
        if c.isdigit():
            if not number_started:
                if c == '0':
                    return False
            number_started = True
    return True

main()