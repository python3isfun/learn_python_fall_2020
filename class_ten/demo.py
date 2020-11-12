

def print_value(value):
    print("Hello, " + value)
    s = input()
    print ("Your name is " + s)
    return s

x = 4
x = print_value("please tell me your name")
print ("I got this from my function " + x)


def convert_to_celcius(farenheit):
    return 10