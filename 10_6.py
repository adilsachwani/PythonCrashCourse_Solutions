prompt1 = 'Enter first number: '
prompt2 = 'Enter second number: '

number1 = input(prompt1)
number2 = input(prompt2)

try:
    number1 = int(number1)
    number2 = int(number2)

except ValueError:
    print("Kindly enter number as input only!")

else:
    print("Result is " + str(number1+number2))