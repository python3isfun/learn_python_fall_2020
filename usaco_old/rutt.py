n = input()
cs = []
for i in  range(0, int(n)):
    t = input().split()
    cs.append((t[0], int(t[1]), int(t[2])))

# print (cs)

def find_amount(c, cs):
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
        else:
            # c is going north
            if c[2] < t[2] and c[1] > t[1] and (t[2] - c[2]) > (c[1] - t[1]):
                # found a match
                cur_limit = t[2] - c[2]
                if limit is None or limit > cur_limit:
                    limit = cur_limit
    if limit is None:
        limit = "Infinity"
    return limit


for c in cs:
    print (find_amount(c, cs))
