def main():
    text = input("What time is it? ")

    convertred_time = convert(text)
    if convertred_time >= 7 and convertred_time <= 8:
        print("breakfast time")
    elif convertred_time >= 12 and convertred_time <= 13:
        print("lunch time")
    elif convertred_time >= 18 and convertred_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60



if __name__ == "__main__":
    main()