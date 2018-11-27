'''

Written by Avinash S. Soor
Git: Avinasho
12-October-2018

The following code will allow the user to input a string, which the  code will
then reverse.

'''


input_string = input('Please enter a string to reverse: ')
''' This line allows the user to enter the string they want to have reversed.'''

print(' ')
print('Reversing the string: ', input_string)

split_str = input_string.split()
''' This line splits up each word in the input string wherever there is a space,
    and creates a list of all of these words.'''

split_str.reverse()
''' This line reverses the order of the list, so that the words are in the
    correct order when output - however it still needs to be a string.'''

output_str = ''
''' This pre-allocates a string which  will have the final result - doing so
    before the loop prevents it from being overwritten at eact iteration.'''

for i in range(len(split_str)):
    ''' Incrementing over each word in the list...'''
    output_str += split_str[i]
    '''... the current word is added to the string...'''
    output_str += ' '
    '''... as well as a space to separate each word.'''

print(' ')
print('The reversed string is: ')
print(output_str)
'''And finally the reversed string is outputted.'''
