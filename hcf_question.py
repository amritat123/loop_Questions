n1=int(input("any number"))
n2=int(input("any number"))
if n1>n2:
	c=n1
else:
	c=n2
i=1
while i<c:
	if n1% i==0 and n2% i==0:
		hcf=i
	i=i+1
print("hcf value is",hcf)