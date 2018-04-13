a = input("Enter values in the array ")
a = [int(x) for x in a.split(" ")]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[j]<a[i]):
           a[i]=a[i]+a[j]
           a[j]=a[i]-a[j]
           a[i]=a[i]-a[j]

print(a)
