

lines= []
with open("gifts.in", "r") as fin:
    for line in fin:
        lines.append(line.rstrip())

print (lines)

d = {}
for i in range(0, 5):
    # Helena 10
    fields = lines[i].split()
    # ["Helena", "10"]
    name = fields[0]
    # "Helena"
    money = int(fields[1])
    # 10
    d[name] = money
    # d["Helena"] = 10
print (d)

for i in range(5, 10):
    # "Helena Aidan 2"
    # "Olivia Vincent 3"
    fields = lines[i].split()
    # ["Helena", "Aidan", "2"]
    from_friend = fields[0]
    # Helena
    to_friend = fields[1]
    # Aidan
    money = int(fields[2])
    # 2
    #d["Helena"] = d['Helena'] - 2
    d[from_friend] = d[from_friend] - money
    #d["Aidan"] = d["Aidan"] + 2
    d[to_friend] = d[to_friend] + money

print (d)
