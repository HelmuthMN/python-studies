filename = 'reading_files/guest.txt'
name = input("What's your name?\n")

with open(filename, 'a') as file_object:
    file_object.write(f"{name}\n")