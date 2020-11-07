


# necklace = "rrr"

# necklace = "bwr"
# necklace = "wwbr"

def process(necklace):
    reverse_necklace = necklace[::-1]

    counter_one = count_necklace(necklace)
    counter_two = count_necklace(reverse_necklace)

    print (counter_one)
    print (counter_two)
    sum = counter_one + counter_two
    return sum


# problem: how many beads can be collected from left to right.
def count_necklace(necklace):
    previous_beads_color = None

    counter = 1
    for current_bead in necklace:
        print (current_bead)
        if current_bead == "w":
            print ("current bead is white")
            counter = counter + 1
        elif previous_beads_color == None:
            print ("this only runs for the first loop")
            previous_beads_color = current_bead
        else:
            if previous_beads_color != current_bead:
                print ("different bead is encountered, stop the loop")
                break
            else:
                counter = counter + 1
                print ("current bead color is the same as previous bead color")

    return (counter)


s = "wwwbbrwrbrbrrbrbrwrwwrbwrwrrb"

max_n = 0
for i in range(0, len(s)):
    # go through all cuts, current cutting position is i
    cs = s[i:] + s[:i]
    n = process(cs)
    if max_n < n:
        max_n = n

print (max_n)