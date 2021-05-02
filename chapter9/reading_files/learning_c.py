filename = 'reading_files/learning_python.txt'

with open(filename) as file_object:
    for i in file_object:
        print(i.replace('Python', 'C'))