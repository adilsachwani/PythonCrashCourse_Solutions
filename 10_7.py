prompt1 = 'Enter first number: '
prompt2 = 'Enter second number: '

while True:

    number1 = input(prompt1)
    if number1 == 'q':
        break

    number2 = input(prompt2)
    if number2 == 'q':
        break

    try:
        number1 = int(number1)
        number2 = int(number2)

    except ValueError:
        pass

    else:
        print("Result is " + str(number1+number2))

    print()