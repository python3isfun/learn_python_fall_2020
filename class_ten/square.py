"""
ID: dayonghuang
LANG: PYTHON3
TASK: square
"""

lines = []
with open("square.in", "r") as fin:
    for line in fin:
        lines.append(line)

s = lines[0].rstrip()
t = lines[1].rstrip()

x_one = s.split()[:2]
x_two = s.split()[2:]

y_one = t.split()[:2]
y_two = t.split()[2:]

min_x = 1000
min_y = 1000
max_x = 0
max_y = 0

for i in (x_one, x_two, y_one, y_two):
    x = int(i[0])
    if min_x > x:
        min_x = x
    if max_x < x:
        max_x = x

    y = int(i[1])
    if min_y > y:
        min_y = y
    if max_y < y:
        max_y = y

diff_x = max_x - min_x
diff_y = max_y - min_y

n = 0
if diff_x > diff_y:
    n = (diff_x * diff_x)
else:
    n = (diff_y * diff_y)

with open ("square.out", "w") as fout:
    fout.write(str(n))
    fout.write("\n")