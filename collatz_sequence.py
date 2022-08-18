"""
Created on 2022, 18 Aug (18/08/22) at 19:51
    Title: collatz_sequence.py - ...
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules


# Importing Custom Modules


#### Function Definitions ####
def collatz(num):
	if (num % 2) == 0:
		return (num//2)
	else:
		return (3*num + 1)
####

n = int(input('Enter the Number:'))
x = collatz(n)

while x != 1:
	print(x)
	x = collatz(x)
print(x)