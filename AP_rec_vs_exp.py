import time
print("AP rec vs Exp")


def AP(  a ,  d ,  n):
	print("starting func AP")
	k=a
	i=a
	while i<=n:
		print(k)
		k=k+d
		i+=1

	
#def exp(a,d,n):
	
	
print("1.Rec or 2.Exp")
choice=input()

if choice==1:
	a=int(  input("Enter First term")   )
	d=int(  input("Enter Common Diff")   )
	n=int(  input("Enter Number of terms")   )
	print("time started")
	AP(a,d,n)
	end=time.time()
	dur=end-start
	print("dur:", dur)
