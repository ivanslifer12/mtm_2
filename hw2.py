f = open('input.txt', 'r')

citizens = []
candidates = []
supports = []
for line in f:
    if line == city:
        line += 1
        city = line.split(",")
    if line == 'citizens':
        while line+1 != 'candidates':
            line += 1
            citizens.append([line.split(",")])
    if line == 'candidates':
        while line+1 != 'support':
            line += 1
            candidates.append([line.split(",")])
    if line == 'output':
        line += 1
        out = line.split(",")

print(city)
print(citizens)
print(candidates)
print(out)


