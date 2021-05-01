products_data = input()
products = {}
while not products_data == "buy":
    name, price, quantity = products_data.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price

    products_data = input()

for key, value in products.items():
    total_price = value["price"] * value["quantity"]
    print(f"{key} -> {total_price:.2f}")
