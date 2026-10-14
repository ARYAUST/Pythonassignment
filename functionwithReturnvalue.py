def calculate_bill(price, quantity):
    total = price * quantity

    if total > 2000:
        total = total - (total * 0.10)  # 10% discount

    return total

# Example
print(calculate_bill(500, 5))