print("Factorial of a number")
x=int(input('Enter a number'))
def fact(x):
	i=1
	j=1
	while(i<=x):
		j=j*i
		i=i+1
	print('The factorial of the no. is',j)


fact(x)