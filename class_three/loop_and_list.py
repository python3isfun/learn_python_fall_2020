
# show case of basic for loop

s = "apple"
# s= "apple is bad"


print (len(s))

print (s[0])
print (s[1])
print (s[2])
print (s[3])
print (s[4])

print (s[99]) # ??? This will cause problem


# first for loop
for i in s:
    print (i)


# loop over a longer string

s = "today is a good day"
print (len(s))
for i in s:
    print (i)

# loop of a list of words
s = ["today", "is", "a", "good day"]

for i in s:
    print (i)

# convert a long string to a list of words using split()
s = "today is a good day"
print (s)
s = s.split()
print (s)


# for loop iterating over a list of numbers
fahrenheit_degrees = [1, 1, 5, 1, 1]
fahrenheit_degrees = [10, 15, 22, 100, 30]


# iterate over a list of numbers and takes average degrees
total = 0
for d in fahrenheit_degrees:
    print ("current degree in Fairenheit is %s" % d)
    total = total + d

avg_degree = total / len(fahrenheit_degrees)
print (avg_degree)
c = (d - 32) * 5 / 9
print ("current degree in Celsius is %s" % c)


# sum over the loop with dollar allowrance example
dollar_allowrance = [10, 15, 22, 100, 30]
total = 0
for a in dollar_allowrance:
    print ("current allowrance total is %s" % total)
    total = total + a
    print ("after adding, current allowrance total is %s" % total)

print ("final total is %s" % total)

# showcase of while loop
while total < 1000:
    total = total + 100
    print (total)
print ("final total %s" % total)

