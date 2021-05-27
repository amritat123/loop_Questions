n=11
sum=0
average=0
while n>0:
	num=int(input("any number"))
	sum=sum+num
	average=sum/11.0
	n=n-1
print(average)
if average%5==0:
	print("yes")
else:
	print("no")