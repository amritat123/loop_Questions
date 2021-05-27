num=int(input('enter any number'))
a=0
b=1
i=1
print(a)
while i<=num:
	c=a+b
	a=b
	b=c
	print(a)
	i+=1