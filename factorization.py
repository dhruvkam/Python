def check(a,b,c):
	if c==a+b:
		return 1
	elif c==a-b:  
		return 2
	elif c==b-a: 
		return 3
	elif c==-a-b:
		return 4
	else:
		return 0
	
while True:
	print("STEP I:")
	a=int(input("a="))
	b=int(input("b="))
	c=int(input("c="))
	suma=b
	product=a*c
	print("\nSTEP II")
	print ("Sum should be ", suma, "And Product should be ", product)
	producta=abs(product)
	print("\nSTEP III")
	print("Factorizing....")
	n=producta
	counter=0
	while producta>0:
		if (n)%(producta)==0:
			
			if check(producta, n//producta, suma)==0:
				print (producta, " x ", n//producta)
			if check(producta, n//producta, suma)==1:
				print (producta, " x ", n//producta, "  YES!")
				#print ("one")
				x=producta
				y=n//producta
				z=1
			if check(producta, n//producta, suma)==2:
				print (producta, " x ", n//producta, "  YES!")
				#print ("two")
				x=producta
				y=n//producta
				z=2
			if check(producta, n//producta, suma)==3:
				print (producta, " x ", n//producta, "  YES!")
				#print ("three")
				x=producta
				y=n//producta
				z=3
			if check(producta, n//producta, suma)==4:
				print (producta, " x ", n//producta, "  YES!")
				#print ("four")
				x=producta
				y=n//producta
				z=4
			else:
				print("Not Factorizable  :(")
		producta=producta-1
		
	#print(x)
	#print(y)
	#print(z)
	if z==2: 
		y=y*-1
	if z==3:
		x=x*-1
	if z==4:
		x=x*-1
		y=y*-1
	print("\nSTEP IV:")
	print ("Hence ",suma," = ", "?",abs(x) ,"+", "?",abs(y))
	print ("      ",suma," = ", x ,"+", y)
	print("\nSTEP V")
	print('Checking.....')
	print("If x is",x, "f(x) is", a*x*x-b*x+c)
	print("If x is",y, "f(x) is", a*y*y-b*y+c)
	print("Thus the roots are", -1*x, "and", -1*y,"\n\n")
	
	
