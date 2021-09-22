import random
def convert(list):
    res = sum(d * 10**i for i, d in enumerate(list[::-1]))
    return(res)
userid=[]
n=5
for j in range(n):
    userid.append(random.randint(1,10))

newid = convert(userid)