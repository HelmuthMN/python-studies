while True:
    name = input("What`s your name?\n")
    if name.isalpha():
        break
    else: 
        print("Enter a valid name arrombado.\n")
print("\nEnter the date of your birthday bellow: ")
month = input("\nEnter the month: ")
day =  int(input("Enter the day: "))
year = int(input("Enter the year: "))
while True:
    address = input("\nWhat's your address?\n")
    if address.isalpha():
        break
    else:
        print("Enter a valid address.\n")
while True:
    goals = input("\nSay your main goal for your life: \n")
    if goals.isalpha:
        break
    else: 
        print("Enter a valid answer.")


def printBio():
    print(f"- Name: {name}")
    print(f"- Date of birth: {month} {day}, {year}")
    print(f"- Address: {address}")
    print(f"- Personal goals: {goals}")



printBio()