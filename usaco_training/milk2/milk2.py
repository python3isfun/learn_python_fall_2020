"""
ID: dayong.1
LANG: PYTHON3
TASK: milk2
"""

def log(s):
    # print(s)
    pass

lines = []
with open("milk2.in", "r") as fin:
    for line in fin:
        lines.append(line)

n = int(lines[0])
pairs = []
for i in range(1, n+1):
    pairs.append(lines[i].split())


pp = []
for p in pairs:
    fp = int(p[0])
    sp = int(p[1])
    pp.append((fp,sp))

np = []
max_milk = 0
for p in pp:
    # for each pair, find the longest starting from this pair
    fp = int(p[0])
    sp = int(p[1])
    for q in pp:
        fq = int(q[0])
        sq = int(q[1])

        if fq < fp and sq > sp:
            fp = fq
            sp = sq

        if (sp > fq and sp <= sq) or (sp >= fq and sp < sq):
            sp = sq

        if (fp >= fq and fp < sq) or (fp > fq and fp <= sq):
            fp = fq

    log ("current max found for %s is %s" % (fp, sp))
    current_milk = sp - fp
    log ("current milke is %s" % current_milk)

    np.append((fp, sp))
    if max_milk < current_milk:
        max_milk = current_milk

log (np)
max_gap = 0
for p in np:
    # if fp is not in any of the pairs, we have a gap, find the smallest gap ending at fp
    # if sp is not in any of the pairs, we have a gap. find the smallest gap starting at sp
    fp = int(p[0])
    sp = int(p[1])

    current_gap = None
    for q in pairs:
        fq = int(q[0])
        sq = int(q[1])
        gap = None
        if sp < fq:
            gap = fq - sp
        if fp > sq:
            gap = fp - sq
        if current_gap is None and gap is not None:
            current_gap = gap
        if gap is not None and current_gap is not None and current_gap > gap:
            current_gap = gap
    log("for pair %s %s, best gap is %s" % (fp, sp, current_gap))
    if current_gap is not None and max_gap < current_gap:
        max_gap = current_gap

log ("max milk is %s" % max_milk)
log ("max gap is %s" % max_gap)

# log ("max gap is %s" % max_gap)
fout = open("milk2.out", "w")
fout.write("%s %s\n" % (max_milk, max_gap))
fout.close()

# for each starting loop through
# for each starting loop through