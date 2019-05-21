sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizler"]

while True:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()
    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that")
            continue
    except IndexError:
        print("Sorry, there is no more {}".format(choice.upper()))
    else:
    print("Here's your {}: {}".format(choice, snack))
