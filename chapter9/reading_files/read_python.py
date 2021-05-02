filename = 'reading_files/learning_python.txt'

with open(filename) as file_object:
    print(file_object.read())

with open(filename) as file_object:
    for l in file_object:
        print(l)
    
with open(filename) as file_object:
    lines = file_object.readlines()


pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)