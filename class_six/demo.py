

# mod operation %, odd even condition
x = 10
if x % 2 == 1:
    print ("this is an odd number")
elif x % 2 == 0:
    print ("this is an even number")

# len() function on a list
x = [0, 1, 2, 3, 5, "apple", "orange"]
print (len(x))

print (x[6])
print (x[-1])
print (x[len(x) -1])

# range function on a list
## iterate over one million minus one
for i in range(0, 1000000):
    print (i)



# if condition in a loop
## find the smallest number
smallest = None
x = [1, -10, 100, 200, 5]
for i in x:
    if smallest == None:
        smallest = i
    if smallest > i:
        smallest = i
print (smallest)

### grade counting example
ac = bc = cc = dc = fc = 0
for i in x:
    if i >= 90:
        ac = ac + 1
    elif i >=  80:
        bc = bc + 1
print (ac)
print (bc)


# continue a loop
## only print the number only if the number is positive
smallest = None
x = [1, -10, 100, 200, 5]
for i in x:
    if i < 0:
        continue
    print ("only print positive number" + str(i))
print ("all is done")


# break a loop
## stop printing if a negative number appears in the list
smallest = None
x = [1, -10, 100, 200, 5]
for i in x:
    if i < 0:
        break
    print ("only print positive number" + str(i))
print ("all is done")


# write to a file
fout = open('output.txt', 'w')
fout.write("hello python")
fout.close()

