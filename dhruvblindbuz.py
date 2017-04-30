import time 
while True:
	x=int (   input("First no  ")  )
	y=input("Operator " )
	z=int (  input("Second no  " )  )
	if y=='+':
		n=x+z
	elif y=='-':
		n=x-z
	elif y=='*':
		n=x*z
	elif y=='/':
		n=x/z
	print("Answer", n)
	print("")
