x=int(input('enter a number'))
def stgr(x):
	result=help(x,x)
	return result

def help(x,len):
	if x==0:
		return(" ")
	if x==1:
		return("1,0,8")
	m=help(x-2,len)
	result=[]
	for i in m:
		if x!=len:
			result.append("0" + i + "0") 
		result.append("8" + i + "8")
		result.append("1" + i + "1")
		result.append("9" + i + "9")
		result.append("6" + i + "6")
	return result

print(stgr(x))


