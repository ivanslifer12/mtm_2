import mtm_elections
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
me_ptr = mtm_elections.mtmElectionsCreate()
result = mtm_elections.mtmElectionsAddCity(me_ptr, str(city[0]), int(city[1]))
for citizen_i, index in enumerate(citizens):
    result = mtm_elections.mtmElectionsAddCitizen(me_ptr,
                                                  str(citizens[citizen_i][0]),
                                                  int(citizens[citizen_i][1]),
                                                  int(citizens[citizen_i][2]),
                                                  int(citizens[citizen_i][3]),
                                                  int(citizens[citizen_i][4]))
for candidate_i, index in enumerate(candidates):
    result = mtm_elections.mtmElectionsAddCandidate(me_ptr,
                                                    int(candidates[candidate_i][0]),
                                                    int(candidates[candidate_i][1]))
for support_i, index in enumerate(supports):
    result = mtm_elections.mtmElectionsSupportCandidate(me_ptr,
                                                        int(supports[support_i][0]),
                                                        int(supports[support_i][1]),
                                                        int(supports[support_i][2]))
result, mayor_id = mtm_elections.mtmElectionsMayorOfCity(me_ptr,
                                                         int(out[0]),
                                                         str(out[1]))
mtm_elections.mtmElectionsDestroy(me_ptr)

f.close()
