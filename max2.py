
data = [1,2,2,5,-3,-199,44,22,25,56,565,565,23,67]

max1 = data[0]
max2 = data[0]

for d in data:
	if d > max2:
		max1 = max2
		max2 = d
	elif d == max2:
		max1 = d
	else:
		if d > max1:
			max1 = d


print max1,max2
			
