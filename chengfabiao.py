

for i in range(1,10):
	for j in range(1,10):
		if j>i:
			continue
		else:
			#print 'i=%d,j=%d' % (i,j),
			print '%d*%d=%d' % (i,j,i*j),
	print "\n"

