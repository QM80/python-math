r=[2.5,4.0,1000]
x= 1e-5 * len(r)

def logistic(r,x):
    return float(i)*x*(1-x)

for i in r:
    x=0.0001
    for _ in range(8):
        x=logistic(r,x)
        print(x)