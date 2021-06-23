def tu():
	l=list()
	n=int(input("enter number of elements : "))
	for i in range(0,n):
		m=input("enter elements : ")
		l.append(m)
		a=tuple(l)
	return a
while True:
	print("%"*90)
	print("choose your choice : ")
	print("1.concate")
	print("2.repeating")
	print("3.maximum value")
	print("4.minimum")
	print("5.slice")
	print("6.range slice")
	print("7.reverse")
	print("8.length")
	print("9.string membership")
	print("10.delete")
	ch=int(input("enter the choice"))
	print("%"*90)
	if ch==1:
		print("1st")
		a=tu()
		print(a)
		print("2nd") 
		b=tu()
		print(b)
		print("concat")
		print(a+b)
	elif ch==2:
		a=tu()
		print(n1*2)
	elif ch==3:
                a=tu()
                print("maximim value ",max(a))
	elif ch==4:
                a=tu()
                print("min : ",min(a))
	elif ch==5:
		a=tu()
		print(a)
		c=int(input("enter slice number"))
		print(a[c])
	elif ch==6:
		a=tu()
		print(a)
		c=int(input("enter starting range"))
		d=int(input("enter ending range")) 
		print(a[c:d])
	elif ch==7:
		a=tu()
		print(a)
		print(a[::-1])

	elif ch==8:
		a=tu()
		print("length",len(a))
	elif ch==9:
		a=tu()
		c=input("enter the member")
		print(c in a)
	elif ch==10:
		a=tu()
		print(a)
		del a
		print("delete")
	else :
		print("choose valid input")
				
