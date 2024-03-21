def avgfun(*n):
    sums = 0
 
    for a in n:
        sums = sums + a
 
    b = sums / len(n)
    return (b)
