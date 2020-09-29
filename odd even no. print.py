no=int(input("enter the number upto which we need to find odd even\n"))
for i in range(1,no+1):
    if (i % 2 == 0):
        print(i)
        print("even number")
    elif (i % 2 == 1):
        print(i)
        print("odd no.")
    else:
        print("its a decimal value please enter a correct number")
