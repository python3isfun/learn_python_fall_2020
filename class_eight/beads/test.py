
lines = []
with open("beads.in", "r") as fin:
    for line in fin:
        lines.append(line.rstrip())
max_number = 0

s = lines[1]
first_char = None
counter = 1
for i in s:
    s = s[1:] + s[:1]
    if first_char != None:
        print("Loop", str(counter))
    if first_char == None:
        # print("Assigning first char from none to " + str(i))
        first_char = i
        print()
        print('"%s" is the bead variable for now.' % i.upper())
    else:
        if first_char == "w" and i != "w":
            first_char = i
        else:
            if i != first_char and i != 'w':
                print("Output: Different Color")
                print("Loop Stopped")
                break
            else:
                print("Output: Wild Card")

        if i != first_char:
            print("Output: Different Color")
            print("Loop Stopped")
            break
        else:
            print("Output: Same Color")
            counter = counter + 1
    print()
print()
print("Same color beads in a row:", counter)
