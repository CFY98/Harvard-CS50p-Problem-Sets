def coke_machine():
    coin = [25, 10, 5]
    cost = 50
    
    while cost > 0:
        price = int(input(f"Amount Due: {cost}\nInsert Coin: "))

        if price in coin:
            cost -= price
                         
    print(f"Change Owed: {abs(cost)}")
    
coke_machine()
