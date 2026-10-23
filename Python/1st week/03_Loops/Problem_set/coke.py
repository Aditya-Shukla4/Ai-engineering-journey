total_amount = 50;
print("Amount Due: ", total_amount)

while total_amount > 0:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        total_amount -= coin
        print("Amount Due: ", total_amount)
    else :
        print("Amount Due:", total_amount)
        
print("Change Owed:", abs(total_amount))