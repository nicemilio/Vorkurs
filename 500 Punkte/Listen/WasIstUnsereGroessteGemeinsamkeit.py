def ggT (a, b):
    if b == 0:
        return a
    else:
        return ggT (b, a % b)

def kgV (a, b):
    return int (abs (a) * abs (b) / ggT (a, b))

print (ggT (100, 150))
print (kgV (12, 18))
