def process_order(order):
    if "customer" not in order:
        print("Invalid order")
        return

    total = 0

    for item in order["items"]:
        total += item["price"] * item["quantity"]

    if total > 1000:
        discount = total * 0.10
    else:
        discount = 0

    total -= discount

    tax = total * 0.18
    total += tax

    print("Customer:", order["customer"])
    print("Subtotal:", total - tax)
    print("Tax:", tax)
    print("Total:", total)

    with open("orders.txt", "a") as f:
        f.write(f"{order['customer']} - {total}\n")