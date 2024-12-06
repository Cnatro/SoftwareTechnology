
def stats_cart(cart):
    total_quantity,total_prices = 0,0
    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_prices += c['quantity'] * c['price']

    return {
        "total_quantity":total_quantity,
        "total_prices":total_prices
    }