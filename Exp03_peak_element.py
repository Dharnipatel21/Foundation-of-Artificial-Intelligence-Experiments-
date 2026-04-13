#3 peak element
import math
import cmath
def find_peak(arr):
   l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < arr[m + 1]:
            l = m + 1
        else:
            r = m
    return arr[l]
p = [10, 5, 16, 1, 2]
peak = find_peak(p)
sqrt_peak = cmath.sqrt(peak)
print(peak, round(sqrt_peak.real, 2) + round(sqrt_peak.imag, 2) * 1j)
