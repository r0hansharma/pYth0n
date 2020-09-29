no=int(input('enter the no to check\n'))
if(no>1):
    for i in range(2 , no):
        if(no%i==0): print(no,'is not a prime number')
        else:
            print( no,"is a prime number")
elif(no==1):
    print("1 is neither a prime nor a compposite number")
else:
    print("enter a number greater than 1")