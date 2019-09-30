s=[1,1,1,2,2,3,4,4,4,1]
d={ }
for x in s:
     val=d.get(x)
     if val:
        d[x]=val+1
     else:
         d[x]=1
print(d)