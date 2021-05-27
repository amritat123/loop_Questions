num=int(input("enter the any number"))
i=1
while num>0:
	digit=num%10
	i=i*digit
	num=num//10
print(i)