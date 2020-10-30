

############################################
# shift a sentence by character.
############################################

x = "apple is good"

for i in range(0,len(x)):
    print ("... ... currently shifting " + str(i) + "th character")
    print (x[i:] + x[:i])

