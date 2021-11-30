print("Welcome to the Shipping Accounts Program")
usernames = ["eramom", "footea", "davisv", "papinukt", "allenj"]
name = input("Hello, what is your username: ").lower()
if name in usernames:
    print(f"""
    Hello {name}. Welcome back to your account.
    Current shipping prices are as follows:
    
    Shipping orders 0 to 100:       $5.10 each
    Shipping orders 100 to 500:     $5.10 each
    Shipping orders 500 to 1000:    $5.10 each
    Shipping orders over 1000:      $5.10 each
    """)
    quantity = int(input("How many items would you like to ship: "))
    total_cost = 0
    cost = 0
    if quantity > 100:
        cost = 5.10
        total_cost = round(cost * quantity, 2)
    elif 100 < quantity < 500:
        cost = 5.00
        total_cost = round(cost * quantity, 2)  
    elif 500 < quantity < 1000:
        cost = 4.95
        total_cost = round(cost * quantity, 2)
    elif quantity > 1000:
        cost = 4.80
        total_cost = round(cost * quantity, 2)

    print(f"To ship {quantity} items it will cost you ${total_cost} at ${cost} per item.")
    place_order = input("Would you like to place this order (y/n): ").lower()
    if place_order == "y":
        print(f"Great. Shipping your {quantity} items.")
    else:
        print("No order has been placed.")           
else:
    print("Sorry, you don't have an account with us. Goodbye.")
    