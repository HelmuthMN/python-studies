from random import randint

def main():    
    choice = ["rock","paper","scissors"]
    computer = choice[randint(0,2)]

    while True:
        player = input("Your choice: ").lower()
        if player in choice:
            print(f"COM: {computer}")
            checkInput(player, computer)
            break
        else:
            print("Enter a valid input.")

def checkInput(p, c):
    if p == c:
        print("Draw")
    elif p == "rock" and c == "paper":
        print("Computer Win")
    elif c == "rock" and p == "paper":
        print("Player Win")
    elif p == "rock" and c == "scissors":
        print("Player Win") 
    elif c == "rock" and p == "scissors":
        print("Computer Win")
    elif p == "paper" and c == "scissors":
        print("Computer Win")
    elif c == "paper" and p == "scissors":
        print("Player Win")


main()
