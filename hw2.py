
f = open('input.txt', 'r')

citizens = []
candidates = []
supports = []
city = []
out = []

#start of reading

part = ['city', 'citizens', 'candidates', 'supports', 'output']

for line in f:
    if line == 'city\n':
        position = part[0]
    if line == 'citizens\n':
        position = part[1]
    if line == 'candidates\n':
        position = part[2]
    if line == 'support\n':
        position = part[3]
    if line == 'output\n':
        position = part[4]

    if position == 'city':
        if line != 'city\n':
            city = line.rstrip("\r\n").split(",")
    if position == 'citizens':
        if line != 'citizens\n':
            citizens.append(line.rstrip("\r\n").split(","))
    if position == 'candidates':
        if line != 'candidates\n':
            candidates.append(line.rstrip("\r\n").split(","))
    if position == 'supports':
        if line != 'support\n':
            supports.append(line.rstrip("\r\n").split(","))
    if position == 'output':
        if line != 'output\n' and line != '\n':
            out = line.rstrip("\r\n").split(",")

#end of reading

#test for lists
print(city)
print(citizens)
print(candidates)
print(supports)
print(out)

#using mtmelections


f.close()
