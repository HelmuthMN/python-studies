print("Enter the full meaning and we provide the acronym.")
acronym = " "
meaning = input("Full Meaning: ")
phrase = (meaning.replace('of', '')).split()
for word in phrase:
    acronym = acronym + word[0].upper()
print(acronym)