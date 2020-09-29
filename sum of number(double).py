dsnum=int(input("enter the number upto which double sum has to print"))
sum=0
for i in range(1,dsnum+1):
    i=i*2
    sum=sum+i
print("double sum of", dsnum ,"=" ,sum)