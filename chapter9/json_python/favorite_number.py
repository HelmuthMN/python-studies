import json

filename = 'favorite_number.json'
def get_favorite_number():
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def set_favorite_number():
    number = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number

def favorite_number():
    number = get_favorite_number()
    if number:
        print(f"I know your favorite number! It's {number}")
    else:
        number = set_favorite_number()
