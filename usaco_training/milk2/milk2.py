
lines = []
with open("milk2.in", "r") as fin:
    for line in fin:
        lines.append(line)

n = int(lines[0])
pairs = []
for i in range(1, n+1):
    pairs.append(lines[i].split())
print (pairs)
ss = []
es = []
for p in pairs:
    ss.append(int(p[0]))
    es.append(int(p[1]))
print (ss)
print (es)

# for each starting loop through