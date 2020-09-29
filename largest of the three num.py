a=float(input('enter first value\t'))
b=float(input('enter first value\t'))
c=float(input('enter first value\t'))
if ((a>=b) and (a>=c)):
     print(a,'is largest number among',a,b,c)
elif ((b>=a) and (b>=c)):
     print(b,'is largest number among',a,b,c)
else:
     print(c,'is largest number among',a,b,c)