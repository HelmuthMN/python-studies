import random

lottery = ['a', 'e', 'i', 'o', 'u', 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
my_ticket = ['a', 5, 6, 'i']
prize = []
count = 0

while my_ticket != prize:
    for n in range(4):
        temp = random.choice(lottery)
        prize.append(temp)
        lottery.remove(temp) 
    if prize == my_ticket:
        break
    else:
        count += 1
        print(count)
        for i in prize:
            lottery.append(i)
