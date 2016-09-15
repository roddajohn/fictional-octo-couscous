import random

csv = open('occupations.csv').read()

dictionary = dict()

for line in csv.split('\n'):
    if not line == "":
        if line[0] == '"':
            dictionary[line.split('"')[1]] = float(line.split('"')[2].split(',')[1])
        else:
            dictionary[line.split(',')[0]] = float(line.split(',')[1])

def pick_random():
    random_number = random.random()
    random_number = random_number * 99.8

    for key in dictionary:
        if random_number < dictionary[key]:
            print key
            return
        random_number -= dictionary[key]

pick_random()

