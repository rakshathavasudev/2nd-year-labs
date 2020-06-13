x=int(input('Enter a no. x to print the fibonacci  series till x terms'))
a=0
b=1
i=0
def fib(a,b,x,i):
	if x<0:
		print('Enter a positive integer')
	elif x==1:
		print(a)
	else:
		while i<x:
			print(a,end=",")
			c=a+b
			a=b
			b=c
			i+=1

fib(a,b,x,i)



