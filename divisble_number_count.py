i=1
while i<=100:
	count=0
	z=2
	while z<i:
		if i%z==0:
			count=count+1
			break
		z=z+1
	if count==0:
			print(i)
	i=i+1