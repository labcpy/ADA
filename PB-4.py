def fractional_knapsack(W, items):
    items.sort(key=lambda x: (x[0] / x[1]), reverse=True)
    total_value = 0.0

    for profit, weight in items:
        if weight <= W:
            W -= weight
            total_value += profit
        else:
            total_value += profit * W / weight
            break

    return total_value

W = 50
items = [(100, 10), (120, 20), (60, 30)]
max_value = fractional_knapsack(W, items)
print(max_value)
