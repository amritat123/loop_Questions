num=int(input("any number"))
rem=0
sum=0
n=num
while num>0:
	rem=num%10
	sum=sum+rem
	num=num//10
if n%sum==0:
	print("harshad number h")
else:
	print("nhi h")