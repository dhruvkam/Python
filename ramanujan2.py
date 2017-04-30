def cub(a):
	b=a**(1/3)
	d=int (b) +1
	#print("Cub=", d-1)
	c=list(range(d))
	#print(c)
	#c.remove(c[0])
	#print(c)
	chek(a,c)
def chek(orig,a):
	#print("Starting chek with list:",a)
	leng=len(a)
	#print("leng of list:",leng)
	x=1
	y=x+1
	count=0
	while x<=leng:
		while y<=leng:
			z=x**3+y**3
			if z==orig and count==1:
				print(orig," =", p, "**3 + ", q,"**3")
				print(orig," =", x, "**3 + ", y,"**3\n")
			if z==orig:
				p=x
				q=y
				count=count+1
				#if count==2:
					#print("count 2 for",orig)
					#print(orig," is", p, "cubed plus", q,"cubed, count:",count)
					#print(orig," is", x, "cubed plus", y,"cubed, count:",count)
			y=y+1
		x=x+1
		y=x+1
	count=0
n=0		
while n<200000:
	cub(n)
	n=n+1
