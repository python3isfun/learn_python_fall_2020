"""
ID: dayong.1
LANG: PYTHON3
TASK: friday
"""

def log(s):
    pass


lines = []
with open("friday.in") as fin:
    for i in fin:
        lines.append(i)
# print (lines)
n = int(lines[0])
ty = 1900 + n

total_days = 0
dom = 0 # day of month
result = {}

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
for i in range(0, 7):
    result[week[i]] = 0
for i in range(1900, ty):
    leap = (i % 4 == 0) and not (i % 100 == 0 and int(i/100) % 4 != 0)
    y = 365
    n = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap:
        n = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y = 366
    s = []
    k = 0
    for ns in n:
        k = ns + k
        s.append(k)
    log ("for year %s, s list is %s" % (i, s))
    for doy in range(1, y+1):
        # doy 1 to 365, doy is day of year
        total_days = total_days + 1
        found = False
        dom = -1
        # find which day is in the month
        moy = 0
        log ("today is %s" % total_days)
        while found == False:
            if s[moy] >= doy:
                if moy == 0:
                    dom = doy
                else:
                    dom = doy - s[moy - 1]
                found = True
            moy = moy + 1


        if dom == 13 :
            result[week[total_days % 7 - 1]] += 1
            log("for year %s, doy %s current moy is %s dom is %s, dow %s" % (i, doy, moy , dom, week[total_days % 7 - 1]))
vs = []
for k, v in result.items():
    vs.append(str(v))

log (result)
log (' '.join(vs[5:] + vs[:5]))
fout = open("friday.out", "w")
fout.write(' '.join(vs[5:] + vs[:5]))
fout.write('\n')
fout.close()
        # NEED TO COUNT CURRENT MONTH, I.E., so we know dom