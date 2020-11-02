"""
ID: dayong.1
LANG: PYTHON3
TASK: milk2
"""

def log(s):
    print(s)


lines = []
with open("milk2.in", "r") as fin:
    for line in fin:
        lines.append(line)

n = int(lines[0])
pairs = []
for i in range(1, n+1):
    pairs.append(lines[i].split())

session_start = 0
session_end  = None

for p in pairs:
    fp = int(p[0])
    sp = int(p[1])
    if session_end is None:
        session_end = sp
    elif session_end < sp:
        session_end = sp

np = []
max_milk = 0
for p in pairs:
    # for each pair, find the longest starting from this pair
    fp = int(p[0])
    sp = int(p[1])

    log ("testing fp %s sp %s" % (fp, sp))
    end = False
    max_second = sp
    while not end:
        # keep looping the list untill not more second is foun
        found_second = False
        for q in pairs:
            fq = int(q[0])
            sq = int(q[1])
            log("testing fq %s sq %s with max_second %s" % (fq, sq, max_second))

            if max_second < fq and max_second < sq:
                found_second = True
                max_second = sq

        if not found_second:
            end = True
    log ("current max found for %s is %s" % (fp, max_second))
    current_milk = max_second - fp
    np.append((fp, max_second))
    if max_milk < current_milk:
        max_milk = current_milk

log (np)
gaps = []


inverse = []
for n in np:
    if (session_start != n[0]):
        inverse.append((session_start, n[0]))
    if (n[1] != session_end):
        inverse.append((n[1], session_end))

log (inverse)
max_gap = 0
for p in pairs:
    # if fp is not in any of the pairs, we have a gap, find the smallest gap ending at fp
    # if sp is not in any of the pairs, we have a gap. find the smallest gap starting at sp
    fp = int(p[0])
    sp = int(p[1])

    log ("testing fp %s sp %s" % (fp, sp))
    end = False
    min_second = sp
    while not end:
        # keep looping the list untill not more second is foun
        found_second = False
        for q in pairs:
            fq = int(q[0])
            sq = int(q[1])
            log("testing fq %s sq %s with max_second %s" % (fq, sq, max_second))

            if min_second > fq and min_second < sq:
                found_second = True
                min_second = fq

        if not found_second:
            end = True
    log ("current min found for %s is %s" % (fp, min_second))
    current_gap = min_second - fp
    if max_gap < current_gap:
        max_gap = current_gap

# max_gap = 0
# for i in np:
#     fi = i[0]
#     si = i[1]
#     for j in np:
#         fj = j[0]
#         sj = j[1]
#
#         gap = 0
#         if fi > sj:
#             gap = fi - sj
#         elif fj > si:
#             gap = fj - si
#         print ("for i %s %s, j %s %s, gap is %s" % (fi, si, fj, sj, gap))
#         if max_gap < gap:
#             max_gap = gap

log ("max milk is %s" % max_milk)
log ("max gap is %s" % max_gap)
fout = open("milk2.out", "w")
fout.write("%s %s\n" % (max_milk, max_gap))
fout.close()

# for each starting loop through
# for each starting loop through