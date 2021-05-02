filename = 'reading_files/guest_book.txt'

n = 0

while n < 10:
    name = input("Enter your name: ")
    print(f"Welcome {name}!!")

    with open(filename,'a') as file_object:
        file_object.write(f"{name} are registered.\n")

    n += 1