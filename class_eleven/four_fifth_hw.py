'''

problem 1:
Create a python dictionary recording the following:
    Read a file called temp.in.
    Each line of the file is a degree in celsius.
    Create a dictionary, using the celsius degree as key, fahrenheit degree as value.

    temp.in:
    0
    20
    100

    The printed dictionary should output:
    {0: 32, 20:68, 100:212}
'''

# lines = []
# with open ("temp.in") as fin:
#     for line in fin:
#         lines.append(line.rstrip())
#
# print (lines)
# d = {}
# for c in lines:
#     celsius = int(c)
#     fahrenheit = celsius * 9 / 5 + 32
#     d[celsius] = fahrenheit
# print (d)

'''
Problem 2:
    Read a file called friends.in
    Each line has a name followed by the amount of money the friend owns.

    friends.in

    Helena 10
    Olivia 20
    Brandon 50
    Vincent 33
    Aidan 22

   Create a python dictonary of following:
    The key is the name of the friend.
    The value is the amount of money the student own.

    The dictionary output:
    {'Helena': 10, 'Olivia': 20, 'Brandon': 50, 'Vincent': 33, 'Aidan': 22}

    Then your program needs to add 5 dollars to each friend's wallet, the second dictionary should be:

    {'Helena': 15, 'Olivia': 25, 'Brandon': 55, 'Vincent': 38, 'Aidan': 27}
'''

lines = []
with open("friends.in", "r") as fin:
    for line in fin:
        lines.append(line.rstrip())

print (lines)

d = {}



for line in lines:
    print (line)
    v = line.split()
    print (v)
    print (v[0])
    print (v[1])
    d[v[0]] = int(v[1])
print (d)