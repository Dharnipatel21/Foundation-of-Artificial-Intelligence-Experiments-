def knapsack(w, v, c):
    if c <= 0 or len(w) != len(v):
        return "Invalid input"
    items = [(val, wt) for wt, val in zip(w, v) if wt > 0 and val >= 0]
    total_value = 0
    remaining = c
    for val, wt in items:
        if wt <= remaining:
            remaining -= wt
            total_value += val
    if total_value == 0:
        return "Capacity exceeded"
    return total_value
print(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))
