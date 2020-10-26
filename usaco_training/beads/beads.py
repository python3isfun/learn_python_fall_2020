"""
ID: dayong.1
LANG: PYTHON3
TASK: beads
"""

def log(s):
    pass

lines = []
with open("beads.in", "r") as fin:
    for i in fin:
        lines.append(i)

n = int(lines[0])
st = lines[1]
max = 0
for i in range(0, len(st)):
    s = st[i:] + st[0:i]
    log ("current s %s" % s)
    prev = None
    fwd_count = 0
    for p in s:
        # for each starting in s
        if (prev != None and p == prev) or prev == 'w' or p == 'w':
            fwd_count += 1
        elif prev == None:
            prev = p
            fwd_count += 1
        else:
            break

    prev = None
    r = s[::-1]
    bak_count = 0
    for p in r:
        # for each starting in s
        if (prev != None and p == prev) or prev == 'w' or p == 'w':
            bak_count += 1
        elif prev == None:
            prev = p
            bak_count += 1
        else:
            break

    log ('fwd %s' % fwd_count)
    log ('back %s' % bak_count)
    total = fwd_count + bak_count
    if max < total:
        max = total

log ('final max %s' % max)
fout = open("beads.out", "w")
fout.write(str(max))
fout.write("\n")
fout.close()
