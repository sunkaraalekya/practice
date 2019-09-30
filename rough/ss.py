n=[1,27,-3,45]
for i in range(len(n)-1,0,-1):
    print("i is ",i)
    for j in range(i):
        print("j is",j)
        if n[j]>n[j+1]:
            temp=n[j]
            n[j]=n[j+1]
            n[j+1]=temp
print(n)