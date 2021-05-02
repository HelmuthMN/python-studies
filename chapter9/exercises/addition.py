print("Hello there, this is a addition calculator. Type de two numbers bellow.")
print("Ops, almost forgot, press 'q' to quit the program.")

while True:
    fn = input("Give the first number: ")
    if fn == 'q':
        break
    sn = input("Give the second number: ")
    if sn == 'q':
        break

    try:
        result = int(fn) + int(sn)
    except ValueError:
        print("The value given wasn't a number.")
    else:
        print(result)
