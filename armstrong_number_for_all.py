num =int(input("enter the number"))
sum=0
lenght=len(str(num))
i=num
while i>0:
	    digit=i%10
	    sum=sum+digit**lenght
	    i=i//10
if sum==num:
		    print("it is armstrong number")
else:
	    print("it is not armstrong number")