x, y = 13, 8
try:
    while x > 1:
        print(float(x))
        x, y = x + y, x
except OverflowError as o:
    print(f'Number too big.\nError: {o}')