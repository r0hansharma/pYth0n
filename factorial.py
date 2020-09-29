n=int(input('enter the number whose factorial to be found\n'))
fact=1
if (n==0):
    print('factorial of 0 is 1' )
else:
    for i in range (n ,0,-1):
        fact=fact*i
print("factorial of" ,n, "is" ,fact)