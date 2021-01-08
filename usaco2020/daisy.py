
# n = input()
n  = 4
ps = "1 1 2 3"
ps = ps.split()


ns = []
for p in ps:
    ns.append(int(p))

# how to generate all sublist from ns?

ss = set()
# generate all two-pair combination from ns
for i in range(0, len(ns)):
    for j in range(0, len(ns)):
        if i <= j:
            ss.add((i,j))

print (ss)

count = 0
for s in ss:
    found_avg_flower = False
    if s[0] == s[1]:
        found_avg_flower = True
    else:
        sum = 0
        for k in range(s[0], s[1]+1):
            sum += ns[k]
        avg = sum / (s[1] - s[0] + 1)
        for k in range(s[0], s[1]+1):
            if avg == ns[k]:
                found_avg_flower = True
    if found_avg_flower:
        count += 1

print (count)