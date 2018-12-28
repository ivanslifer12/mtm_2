f = open('input.txt', 'r')

citizens = []
candidates = []
supports =[]
for line in f:
    while line != 'citizens':
        if line == 'city':
            continue
        city = line.split(",")
        continue
    while line != 'candidates':
        if line == 'citizens':
            continue
        citizens.append([line.split(",")])
    while line != 'support':
        if line == 'candidates':
            continue
        candidates.append([line.split(",")])



