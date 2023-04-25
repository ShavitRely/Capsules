#This file gets a result file and print it to the screen
#Ypu need to attach a 'Hello.txt' file to the Dataset
with open('../data/Hello.txt', 'r') as f:
        res = f.read()
        elements = str(res)
with open('../results/result.txt', 'w') as f:
    f.write("This is the result: " + str(elements))

try:
    import sys
    #Parameters
    text_param = sys.argv[1]
    list_parameter = sys.argv[2]
    file_parameter = sys.argv[3] 
    
    with open('../results/result_param.txt', 'w') as f:
        f.write("This is the Text param: " + text_param)
        f.write("\nThis is the List param: " + list_parameter)
        f.write("\nThis is the File param: " + file_parameter)

except ImportError:
    with open('../results/result_param.txt', 'w') as f:
        f.write('Error')
    print("To generate a result figure, please fix the code")
