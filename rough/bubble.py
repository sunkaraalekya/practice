def bubble(n):
    for i in range((len(n)-1),0,-1):
        for j in range(i):
            if n[j]>n[j+1]:
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
n=[90,-1,-8,100]
bubble(n)
print(n)