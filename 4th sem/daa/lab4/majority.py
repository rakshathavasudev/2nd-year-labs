def majority_element(a):
	n = len(a)
	if n == 1:
		return a[0]
	if n == 0:
		return None
	
	k = n//2
	elem1 = majority_element(a[:k])
	elem2 = majority_element(a[k+1:])
	
	if elem1 == elem2:
		return elem1

	count1 = a.count(elem1)
	count2 = a.count(elem2)

	if count1 > k:
		return elem1
	elif count2 > k:
		return elem2
	else:
		return None

print("Should be 1:", majority_element([0,1,0,1,1]))
print("Should be 0:", majority_element([0,0]))
print("Should be None:", majority_element([0,1,1,1,0,0,2]))
print("Should be 0:", majority_element([0,1,1,1,0,0,0,0,2]))
print("Should be None:", majority_element([0,0,1,1]))
print("Should be None:", majority_element([0,0,1,1,2,2,1,1,2]))
print("Should be 2:", majority_element([0,2,2,2,2,2,0,1,1]))