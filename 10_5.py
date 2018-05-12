filepath = 'poll.txt'
prompt1 = 'Your Name? '
prompt2 = 'Why do you like programming? '
prompt3 = 'Another poll? (y/n) '
poll_active = True

while poll_active:
    name = input(prompt1)
    response = input(prompt2)

    with open(filepath,'a') as file_object:
        file_object.write(name.title() + " : " + response + ".\n")

    another_poll = input(prompt3)

    if(another_poll== 'n'):
        poll_active = False