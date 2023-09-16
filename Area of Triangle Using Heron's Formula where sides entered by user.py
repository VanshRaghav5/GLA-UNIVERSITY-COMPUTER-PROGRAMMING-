a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input("Enter side c:"))
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
area=d**(1/2)
print(area)
