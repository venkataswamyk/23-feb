l=[]
n=int(input('enter value:'))
for i in range(0,n):
    x=int(input())
    l.append(x)
min=l[0]
max=l[0]
for i in range(1,n):
    if l[i]>max:
        max=l[i]
    else:
        min=l[i]
print("maximum element is:",max)
print("minimum element is:",min)
