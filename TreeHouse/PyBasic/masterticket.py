SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return number_of_tickets * TICKET_PRICE + SERVICE_CHARGE

while tickets_remaining >= 1:

    print("There are {} tickets remaining".format(tickets_remaining))

    user_name = input("What is your name?:  ")
    number_of_tickets = input("{}, how many tickets do you whant to buy?  ".format(user_name))
    # Expect a ValueError
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as error:
        print("Oh, no, we run into and issue.{} Please try again.".format(error))
    else:
        total_price = calculate_price(number_of_tickets)

        print("The total due for {} tickets is ${}.".format(number_of_tickets, total_price))

        should_proceed = input("Do you want to buy the tickets. Press Y for Yes or N for No: ")

        if should_proceed.upper() == "Y":
            # TODO: Gather credit card information and process it
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you anyway, {}".format(user_name))

print("Sorry, the tickets are all sold out!!! :(")
