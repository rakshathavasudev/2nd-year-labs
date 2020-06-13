x=int(input('Enter 1st no.'))
y=int(input('Enter 2nd no.'))
def hcf(x,y):
	if y==0:
		return x
	else:
		return hcf(y,x%y)
print('GCD of the no.s is :')
print(hcf(x,y))
