filepath = 'guest.txt'
prompt = 'Name: '

guest_name = input(prompt)

with open(filepath,'a') as file_object:
    file_object.write(guest_name.title() + '\n')

