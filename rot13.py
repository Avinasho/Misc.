'''

Written by Avinash S. Soor
Git: Avinasho
18-September-2018

The following code will perform a rot13 encoding of any input .txt file.

'''

LIST1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
LIST2 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# These are simple lists of uppercase and lowercase letters, whose indexes from
# lsts 1 and lists 2 correspond for a rot13 encoding - but therefore coudld also
# be used for decoding.

test_name = input('Please enter the name of the .txt file you wish to encode: ')
# This line allows the user to choose the text file they wish to encode rather
# than editing the code each time.
try:
    test = open(test_name, 'r')
except:
    test = open('test.txt', 'r')
    print('Error: Failed to open  desired file - test file opened instead.')
# This loads the file to a usable format, or failing that the test file.
test = test.read()
result = ''
# Initialisation of the results array.

for i in range(len(test)):
    if test[i] in LIST1:
        ind = LIST1.index(test[i])
        result += LIST2[ind]
    elif test[i] in LIST2:
        ind = LIST2.index(test[i])
        result += LIST1[ind]
    elif test[i] in list1:
        ind = list1.index(test[i])
        result += list2[ind]
    elif test[i] in list2:
        ind = list2.index(test[i])
        result += list1[ind]
    else:
        result += test[i]
# This for loop will loop over every character in the chosen file, and check
# which list the character belongs to. If it were a number or space, then it
# would correspond to the same thing (a numbber or a space), and save this to
# the variable 'result', which then gets saved

# print(result)
encoded_result = open('encoded_file.txt', 'w')
encoded_result.write(result)
encoded_result.close()
# These lines save the encoded results to a new file.
