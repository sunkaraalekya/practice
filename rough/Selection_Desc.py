n=[-1,100,20,-2]
for i in range(len(n)-1,0,-1):
    min=0
    for j in range(1,i+1):
        if n[j]<n[min]:
            min=j

    temp=n[i]
    n[i]=n[min]
    n[min]=temp
    print("Temporary list",n)
print(n)
