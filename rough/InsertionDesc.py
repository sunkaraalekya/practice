n=[-5,6,12,3]
for i in range(1,len(n)):
    key=n[i]
    j=i-1
    while j>=0 and key>n[j]:
        n[j+1]=n[j]
        j-=1
    n[j+1]=key
print(n)