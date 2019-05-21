shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see the list.
    """)


def add_to_list(item):
    shopping_list.append(item)
    print("Item '{}' was added to the list.".format(item))
    print("There are {} items in the list".format(len(shopping_list)))

def show_list():
    if shopping_list:
        print("Here's your list:")
        for item in shopping_list:
            print("* " + item)
    else:
        print("There no items in the list yet")


show_help()

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
        
    add_to_list(new_item)

show_list()
