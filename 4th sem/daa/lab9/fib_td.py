def fib(n,lookup):
	if n==0 or n==1:
		lookup[n]=n

	if lookup[n] is None:
		lookup[n] = fib(n-1,lookup) + fib(n-2,lookup)

	return(lookup[n])

def main():
	n=4
	lookup=[None]*101
	print("The",n,"th fibonacci number is:",fib(n,lookup))

main()