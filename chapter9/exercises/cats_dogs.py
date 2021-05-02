def printAnimal(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

filename = ['exercises/cats.txt', 'exercises/dogs.txt']
for fn in filename:
    printAnimal(fn)
