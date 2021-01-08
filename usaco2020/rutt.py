
cs = []
max_up = 0

# n = input()
# for i in  range(0, int(n)):
#     t = input().split()
#     cs.append((t[0], int(t[1]), int(t[2])))
#     if max_up < int(t[1]):
#         max_up = int(t[1])
#     if max_up < int(t[1]):
#         max_up = int(t[2])


x = ["E 3 5", "N 5 3", "E 4 6", "E 10 4", "N 11 2", "N 8 1"]
x = ["E 1 3", "N 3 2"]
x = ["E 1 3", "N 3 2", "N 2 1"]
x = ["E 0 0", "N 0 1"]

for i in x:
    t = i.split()
    cs.append((t[0], int(t[1]), int(t[2])))
    if max_up < int(t[1]):
        max_up = int(t[1])
    if max_up < int(t[1]):
        max_up = int(t[2])

max_up += 1
# print (cs)

def find_pairs(c, cs):
    # for given call, find all the possible collisions for this cow
    ret = []
    limit = None
    for t in cs:
        if c[0] == t[0]:
            continue
        if c[0] == 'E':
            if c[1] < t[1] and c[2] > t[2] and (t[1] - c[1]) > (c[2] - t[2]):
                # found a match
                cur_limit = t[1] - c[1]
                if limit is None or limit > cur_limit:
                    limit = cur_limit
                    ret.append((c, t, limit))
        else:
            # c is going north
            if c[2] < t[2] and c[1] > t[1] and (t[2] - c[2]) > (c[1] - t[1]):
                # found a match
                cur_limit = t[2] - c[2]
                if limit is None or limit > cur_limit:
                    limit = cur_limit
                    ret.append((c, t, limit))
    if limit is None:
        ret.append((c, None, "infinity"))
    return ret

threats = []
for c in cs:
    threats.append(find_pairs(c, cs))

# print (threats)
min_threats = []
for t in threats:
    min_d = None
    r = None

    for it in t:
        invalid_threats = False
        fit = it[0]
        sit = it[1]
        dit = it[2]
        if dit == "infinity":
            dit = max_up
        elif min_d is None or min_d  > dit:
            min_d = dit
            r = it

        for t_m in threats:
            for im in t_m:
                # print (im)
                fim = im[0]
                sim = im[1]
                dim = im[2]
                if dim == "infinity":
                    dim = max_up
                if sit == fim:
                    if dim < dit:
                        invalid_threats = True
                if fim == sit and fit == sim:
                    invalid_threats = True
        if invalid_threats:
            r = None

    if r is not None:
        min_threats.append(r)

for c in cs:
    found = False
    for t in min_threats:
        if c == t[0]:
            print (t[2])
            found = True
    if not found:
        print ("Infinity")

