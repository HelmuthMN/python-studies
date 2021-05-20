words = []

def reverse(w):
    rev =''.join(reversed(words[i]))

    if rev == words[i]:
        print("Is a palindrome")
    else:
        print("Isn't a palindrome")

for i in range(5):
    while True:
        w = input("Enter a word: ")
        if w.isalpha():
            words.append(w)
            reverse(i)
            break
        else:
            print("Enter a valid input.")
    i += 1


