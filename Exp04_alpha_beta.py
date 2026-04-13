 alpha beta
import math
def alphabeta(d, i, maxp, val, a, b):
    if d == 2:
        return val[i]
    if maxp:
        for j in range(2):
            a = max(a, alphabeta(d+1, i*2+j, False, val, a, b))
            if b <= a:
                break
        return a
    else:
        for j in range(2):
            b = min(b, alphabeta(d+1, i*2+j, True, val, a, b))
            if b <= a:
                break
        return b
values = [3, 15, 36, 9]
print("Optimal Value:", alphabeta(0, 0, True, values, -math.inf, math.inf))
