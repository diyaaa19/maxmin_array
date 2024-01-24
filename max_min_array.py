a=[]
max=0
min=0
for i in range(0,5):
    b=int(input("enter array element : "))
    a.append(b)

print(a)

for i in range (0,4):
    if a[i]>a[i+1]:
        max=a[i]
    else:
        min=a[i]

print("Maximum Element:",max)
print("Minimum Element:",min)