from showbits import shorthand, bits

print('question 7:')
shorthand(b'2 Faced') #output: 32 20 46 61 63 65 64
#check question 1

print('question 9:')
bits(104) #output: 1101000
shorthand(104) #output: 68
#check question 3

print('question 11:')
bits(b'\xbeef') #output: 10111110 01100101 01100110
shorthand(b'\xbeef') #output: be 65 66
#check question 5

#print('question 13:')
#13 a) type(i) = int
#13 b) type(int) = type
#13 c) INT is a type that stores a whole number, and TYPE is a type that stores a type. They're different because they contextualize data differently; 0x0F could be 15 or it could represent the specific type of a variable.

#print('question 15:')
# 15 a) 01 04 01 05 01 0A 01 07 00
# 15 b)
"""
message = b'\x01\x04\x01\x05\x01\x0A\x01\x07\x00'

print('question 17:')
It could be argued that the bytes are meant to be ascii since both represent a valid ASCII code,
but there are still no guarantees that it's ASCII from the bytes alone.
There are also not guarentees that the bytes were meant to be an int.

One possible solution would be to send some information imediately before or after the bytes were sent that indicate what they are.
For instance, the sent bytes could be preceeded by a byte that communicates the contents of the bytes. 0x00 could indicate ascii and 0x01 could communicate an int.

So the message would be 00 42 41 if it were meant as BA or 01 41 42 if it were meant as 16961
"""

print('question 19:')
i = 0x32204661636564
print(i.to_bytes(7, 'big').decode('ASCII'))

#print('question 21:')
#will do once question 12 done

print('question 22:')
#prediction: e
i = 1000
print(i.to_bytes(2, 'little'))
#prediction: correct

#print('question 23:')
#user_says = input('Please enter the length of the file')
#file_length = int(user_says)

#print('question 25:')
# to_bytes() converts an integer into its numerical representation as bytes whereas...
# encode() converts a string into its ASCII representation in bytes.

print('question 27:')
#cited: nothing
def my_int(input):
    output = 0
    for i in range(0, len(input)):
        output += (input[i]-48) * (10 ** (len(input)-i-1))
    return output
print(my_int(b'1232321'))

#print(question 29:)
"""
I enjoyed solving the questions that involved writing python (questions 27, 22, etc).
The questions that expected specific hand-written answers are necessary to learn the material, so they should remain.
"""
