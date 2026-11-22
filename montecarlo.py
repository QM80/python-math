import random, math
n=1
while n<1000:
    h = sum(1 for _ in range(n) if random.randint(1,10) + random.randint(1,10) <= 10)
    p=h/n
    se=math.sqrt(p*(1-p)/n)
    n+=1
    print(f"{n}: {se}")