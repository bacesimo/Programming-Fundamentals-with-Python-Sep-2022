number_messages = int(input())
messages = ''
for message in range (number_messages):
    number = int(input())
    if number == 88:
        messages = "Hello"
    elif number == 86:
        messages = "How are you?"
    elif number < 88 and number != 86:
        messages = "GREAT!"
    else:
        messages = "Bye."
    print(f"{messages}")