"""
ID: dayong.1
LANG: PYTHON3
TASK: beads
"""

########################################################################
# read input routine
lines = []
with open("beads.in", "r") as fin:
    for line in fin:
        lines.append(line.rstrip())
max_number = 0

s = lines[1]
s = "wwwbbrwrbrbrrbrbrwrwwrbwrwrrb"

########################################################################
# shift a string by charcters
for i in range(0, len(s)):
    t = s[i:] + s[:i]
    print (t)


# s = "wwbbrwrbrbrrbrbrwrwwrbwrwrrbw"

########################################################################
# find the number of consequtive beads from start of the string.
###
# test cases
# s = "br"
# s = "bwr"
# s = "wbwr"
left_right_count = 0
first_char = None
counter = 0
for current_char in s:
    print ("loop " + str(counter))
    if first_char == None:
        print ("assigning first char from none to " + str(current_char))
        first_char = current_char
    else:
        if first_char == "w" and current_char != "w":
            first_char = current_char
        else:
            if current_char != first_char and current_char != 'w':
                print ("stop loop")
                print (current_char)
                break
            else: # current i is the same as first_char
                print ("same as first char")
                print (current_char)
    counter = counter + 1
print (counter)
left_to_right_counter = counter


########################################################################
# reverse a string
# right_to_left_counter = 0
# s = s[::-1]
# counter = 0
# for current_char in s:
#     print ("loop " + str(counter))
#     if first_char == None:
#         print ("assigning first char from none to " + str(current_char))
#         first_char = current_char
#     else:
#         if first_char == "w" and current_char != "w":
#             first_char = current_char
#         else:
#             if current_char != first_char and current_char != 'w':
#                 print ("stop loop")
#                 print (current_char)
#                 break
#             else: # current i is the same as first_char
#                 print ("same as first char")
#                 print (current_char)
#     counter = counter + 1
# right_to_left_counter = counter
#
# print ("left to right " + str(left_to_right_counter))
# print ("right to left " + str(right_to_left_counter))
#
#


########################################################################
# output routine
# #
# # fout = open("beads.out", "w")
# # fout.write(str(max_number))
# # fout.write("\n")
# # fout.close()
