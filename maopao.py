

data = [1,4,2,5,7,2,5,67,3,64,34,23,5654,32,2,6]

for i in range(0,len(data)-2):
	for j in range(0,len(data)-1-i):
		if (data[j] > data[j+1]):
			data[j],data[j+1] = data[j+1],data[j]
	print data,j
	
