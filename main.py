#This file gets a result file and print it to the screen
#Ypu need to attach a 'Hello.txt' file to the Dataset
with open('../data/TESTfile/Hello.txt', 'r') as f:
        res = f.read()
        elements = str(res)
with open('../results/result.txt', 'w') as f:
    f.write("This is the result: " + str(elements))
