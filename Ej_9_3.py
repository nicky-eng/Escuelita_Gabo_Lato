
"""Nicky's Black Book of phone numbers."""

phone_book = {'nicky': +4581907003, 'gabo': 45821097, 'marti': 44319121, 'beba': 49023155}

name = '' #We initilize the empty variable for the while loop to work.

while name != '*':
    name = input("Enter name to add/check (enter * to exit)").lower() #We lowercase the whole word to avoid comparisson problems later.
    if name in phone_book:
        print(phone_book[name])
        change = input("Do you wish to change {}'s phone number? (yes to change, ENTER to continue)".format(name.title()))
        if change.lower() == 'yes':
            phone_book[name] = input("Type new phone number for {}:".format(name.title()))
    elif name != '*':
        phone_book[name] = input("{} is not on the book. Please enter {}'s phone number:".format(name.title(), name.title()))
    


