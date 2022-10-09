command = input()

while command != "End":
    current_print = ""
    if command != "SoftUni":
        for i in command:
            current_print += i * 2
        print(current_print)
    command = input()