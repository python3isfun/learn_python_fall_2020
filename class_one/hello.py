
#
# x = "apple"
#
# x = 10
#
# x  = 10 + 5
#
# x = "apple " + " orange"
#
# # x = "apple " + 10
#
# x  = 10 / 3
#
# print (x)

# Alex
# fahrenheit degree 55
# celsius degree ?

# fahrenheit degree 60
# celsius degree
# fahrenheit_degree = 32
# c = (fahrenheit_degree - 32) * 5 / 9
# print (c)

x = input("Please input celsius degree number: ")
celsius_degree = int(x)
f = celsius_degree * 9 / 5 + 32
print ("The Fahrenheit degree is ")
print (f)

if f < 60:
    print ("this is very cold")
else:
    print ("this is not so cold")


