"""
Created on 2022, 18 Aug (18/08/22) at 19:51
    Title: collatz_sequence.py - Printing Collatz Sequence of a Number
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
...

# Importing Custom Modules
...

#### Function Definitions ####
def collatz(num):
	if (num % 2) == 0:
		return (num//2)
	else:
		return (3*num + 1)
####

input = input('Enter the Number:')

try:
	n = int(input)
	x = collatz(n)
	while x != 1:
		print(x)
		x = collatz(x)
	print(x)

except ValueError:
	print('The number must be Integer')