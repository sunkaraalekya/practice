n=[-100,400,200,-300]
for i in range(1,len(n)):
    key=n[i]
    j=i-1
    print("== {} == {}".format( i, key))
    while j>=0 and key<n[j]:
        n[j+1]=n[j]
        print("In loop ", j , n)
        j-=1
    n[j+1]=key
    print("after loop, ", j, j+1, n)
    print("=============")
print(n)

