def validate_order(order: dict) -> bool:
    """
    Check whether the order contains customer info
    """
    return "customer" in order

def calculate_total(items: list[dict]) -> float:
    """
    Calculate the total of all items
    """
    tot = sum(item["price"] * item["quantity"]for item in items)
    return tot

def calculate_discount(total: float) -> float:
    """
    Return the discount for the order
    """
    if total > 1000:
        return total * 0.10
    return 0.0

def calculate_tax(amount: float) -> float:
    """
    Calculate GST
    """
    return amount * 0.18

def print_receipt(item,discount,tax,total):
    print("="*10)
    print(f"Item : {item}")
    print(f"Discount : {discount}")
    print(f"Tax : {tax}")
    print("="*10)
    print(f"Total : {total}")


def process_order(order: dict) -> None:
    """
    Process an order from start to finish
    """

    if not validate_order(order):
        print("Invalid order")
        return

    total = calculate_total(order["items"])

    discount = calculate_discount(total)

    discounted_total = total - discount

    tax = calculate_tax(discounted_total)

    final_total = discounted_total + tax

    print_receipt(
        order["customer"],
        discounted_total,
        tax,
        final_total
    )