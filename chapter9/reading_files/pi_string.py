filename = 'reading_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday is here!!!")
else:
    print("Your birthday is not here!!!")