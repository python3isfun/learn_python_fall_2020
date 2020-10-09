
ac = bc = cc = dc = fc = 0
with open ("grades.txt", 'r') as fin:
    for i in fin:
        i = int(i)
        if i >= 90:
            ac = ac + 1
        elif i >= 80:
            bc = bc + 1
        elif i >= 70:
            cc = cc + 1
        elif i >= 60:
            dc = dc + 1
        else:
            fc = fc + 1

print ("%s students get A\n%s students get B\n%s students get C\n%s students get D\n%s students get F" % (ac, bc, cc, dc, fc))