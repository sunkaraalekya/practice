n=[-1,30,-2,5]
for i in range(len(n)-1,0,-1):
    print("pass is", i, "subset =", range(1,  i+1))
    max=0
    for j in range(1,i+1):
        print("subset val", j)
        if n[j]>n[max]:
            max=j
            print("max is",max)

    temp=n[i]

    n[i]=n[max]

    n[max]=temp

    print("Semi Sorted Data", n)

print(n)