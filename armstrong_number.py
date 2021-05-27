num =int(input("enter the number"))
2	sum=0
3	i=num
4	while num>0:
5	    digit=num%10
6	    sum=sum+digit**3
7	    num=num//10
8	if sum==i:
9	    print("it is armstrong number")
10	else:
11	    print("it is not armstrong number")