ln=[1,10,5,5,5,7,0,0]
fs=[]
Dict = {}

s=len(ln)
for i,x in enumerate(ln):
    val = Dict.get(x, 0)
    Dict[x] = val + 1

for k, v in Dict.items():
    if v > 1:
        print(k)




