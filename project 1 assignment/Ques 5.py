i1 = int(input("Enter first integer"))
i2 = int(input("Enter second integer"))
i3 = int(input("Enter third integer"))
i4 = int(input("Enter fourth integer"))
i5 = int(input("Enter fifth integer"))
integers = [i1, i2, i3, i4 , i5]
i = 0
sum = 0
while i<5:
    sum=sum+integers[i]
    i=i+1
print(sum)