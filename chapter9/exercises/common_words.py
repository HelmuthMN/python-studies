def book_read(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Nao existe esse livro, arrombado")
    else:
        word = content.count('the ')
        print(word)

filename = ['exercises/dracula.txt', 'exercises/tom_sawyer.txt']
for i in filename:
    book_read(i)
