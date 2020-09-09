

# conditional and indentation

# t = 1
#
# if t == 1:
#     print ("t is 1")
# else:
#     print ("t is not 1")


# Homework 2:
'''
$ python temperature_converter.py
Input temperature: 2f
Got fahrenheit temperature 2 degree
The fahrenheit temperature 2 degree in celsius degree is -16.666666666666668


$ python temperature_converter.py
Input temperature: 23c
Got celsius temperature 23 degree
The celsius temperature 23 degree in fahrenheit degree is 73.4
'''


t = input("Input temperature: ")

if t[-1] == 'f':
    print ("Got fahrenheit temperature %s degree" % t[:-1])
    c = (int(t[:-1]) - 32) * 5 / 9
    print ("The fahrenheit temperature %s degree in celsius degree is %s " % (t[:-1], c))
elif t[-1] == 'c':
    print ("Got celsius temperature %s degree" % t[:-1])
    f = int(t[:-1]) * 9 / 5 + 32
    print ("The celsius temperature %s degree in fahrenheit degree is %s " % (t[:-1], f))
else:
    print ("Temperature must end with c or f!")


# assignment one
# if a user inputs temperature in fahrenheit, convert it to celsius and print out.
# if a user inputs temperature in celsius, convert it to fahrenheit and print out.
