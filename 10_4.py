filepath = 'guest_book.txt'
prompt1 = 'Guest Name: '
prompt2 = 'Another guest? (y/n) '
guest_active = True

while guest_active:
    guest = input(prompt1)
    print("Greetings, " + guest.title() + "!")

    with open(filepath,'a') as file_object:
        file_object.write(guest.title() + "\n")

    another_guest = input(prompt2)

    if(another_guest == 'n'):
        guest_active = False