def collatz(num):
	if (num % 2) == 0:
		return (num//2)
	else:
		return (3*num + 1)

n = int(input('Enter the Number:'))
x = collatz(n)

while x != 1:
	print(x)
	x = collatz(x)
print(x)
