#15 Hill climbing optimization technique
import random
def profit(price):
return -(price - 50)**2 + 2500
def hill_climbing(start, step=1, max_iter=100):
current, value = start, profit(start)
for _ in range(max_iter):
neighbors = [current - step, current + step]
next_pos = max(neighbors, key=profit)
next_val = profit(next_pos)
if next_val <= value:
break
current, value = next_pos, next_val
return current, value
start = random.randint(10, 90)
optimal, max_profit = hill_climbing(start)
print(f"Start: ${start} → Optimal: ${optimal}, Profit: ${max_profit}")
