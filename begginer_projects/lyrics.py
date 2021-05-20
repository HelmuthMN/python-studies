import os

lyrics = {
    "1":"Oh, woah\n\
Oh, woah\n\
Oh, woah\n\
You know you love me, I know you care\n\
Just shout whenever, and I'll be there\n\
You want my love, you want my heart\n\
And we will never, ever, ever be apart",

    "2":"I'm out that H, town coming coming down\n\
I'm coming down, drippin' candy on the ground\n\
H, Town, Town, I'm coming down, coming down\n\
Drippin' candy on the ground...",

    "3":"You’re no better off, living your life and dreaming at night\n\
This much is true, but it’s still up to you to take my advice\n\
To take it slowly, brother\n\
Let it go now, brother\n\
Take it slowly, brother\n\
Let it go",

    "4":"Cracks in the pavement underneath my shoe\n\
I care less and less about and less about you\n\
No one else around to look at me\n\
So I can look at my shadow as much I please\n\
All the kicks that I can't compare to\n\
Making friends like you're all supposed to\n\
You will never come close to how I feel\n\
You will never come close to how I feel"}

while True:
    os.system('cls||clear')    
    print("Welcome, select a song from this list: \n\
    1. Baby by Bieber\n\
    2. Flawless by Beyonce\n\
    3. Brother by MacDemarco\n\
    4. Solitude is Bliss by Tame Impala")

    choose = input("Choose one song: ")
    os.system('cls||clear')
    if choose in lyrics.keys():
        print(lyrics[choose])
    else:
        print("Choose a valid song.")
    
    cnt = input("\nPress * to choose again.\n")
    if cnt == "*":
        continue
    else:
        break

