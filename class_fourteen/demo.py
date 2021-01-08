'''
Given this dictionary representing the student name and the amount of money in his/her wallet:

d =  {'Helena': 15, 'Olivia': 25, 'Brandon': 55, 'Vincent': 38, 'Aidan': 27}
and a list
double_list = {"Brandon", "Helena"}
Write a function to do the following:
    . the function name is called update_wallet
    . the function takes two arguments, the dictionary and the list.
    . the functino should return a new dictionary, such that if the student name is in the double_list,
        double the amount of money. If the student name is not in the list, deduct 3 from his/her wallet.
Example:
    def update_wallet(d, double_list):
        updated_dict = {}
        # write your logic here
        return updated_dict
The final result, given the example input, and when I call the function:
        d =  {'Helena': 15, 'Olivia': 25, 'Brandon': 55, 'Vincent': 38, 'Aidan': 27}
        double_list = {"Brandon", "Helena"}
        d = update_wallet(d, double_list)
        print (d)
    should return
    {'Helena': 30, 'Olivia': 22, 'Brandon': 110, 'Vincent': 35, 'Aidan': 24}
'''


def update_wallet(d, double_list):
    for i in double_list:
        if i in d:
            d[i] = 2 * d[i]

    for k, v in d.items():
        if k not in double_list:
            d[k] = d[k] - 3
    return d

d = {'Helena': 15, 'Olivia': 25, 'Brandon': 55, 'Vincent': 38, 'Aidan': 27}
double_list = {"Brandon", "Helena"}

print (update_wallet(d, double_list))