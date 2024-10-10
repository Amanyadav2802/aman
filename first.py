n1 = int(input("Enter your 1st number"))
n2= int(input("Enter your  2nd number"))
n3= int(input("Enter your 3rd number"))
n4= int(input("Enter your 4th number"))
n5=n = int(input("Enter your 5th number"))
array = [n1,n2,n3,n4]
firstmax = max(array[0], array[1]) 
secondmax = min(array[0], array[1]) 
n = len(array)
for i in range(2,n): 
	if array[i] > firstmax: 
		secondmax = firstmax
		firstmax = array[i] 
	elif array[i] > secondmax and \
		firstmax != array[i]: 
		secondmax = array[i]
	elif firstmax == secondmax and \
		secondmax != array[i]:
		secondmax = array[i]
print("Second highest number in array is: ",
	(secondmax))
