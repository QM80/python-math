r=[1]
for _ in range(10):    l=', '.join(map(str,r)); print(l); r=[l+r for l,r in zip(r+[0],[0]+r)]