x=0
while x<100:
    if x>1 and all(x%i!=0 for i in range(2,x)): print(f"{x} is prime")
    else: pass
    x+=1