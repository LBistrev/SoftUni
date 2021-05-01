command = input()
total_sum = 0
sum_all_prices_without_taxes = 0
taxes = 0

while command != "special" and command != "regular":
    price_without_tax = float(command)
    if price_without_tax < 0:
        print("Invalid price!")
        command = input()
        continue
    else:
        total_sum += price_without_tax + price_without_tax * 0.20
    sum_all_prices_without_taxes += price_without_tax
    taxes = sum_all_prices_without_taxes * 0.20

    command = input()

if command == "special":
    if total_sum == 0:
        print("Invalid order!")
    else:
        total_sum -= total_sum * 0.10
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {sum_all_prices_without_taxes:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_sum:.2f}$")
elif command == "regular":
    if total_sum == 0:
        print("Invalid order!")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {sum_all_prices_without_taxes:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_sum:.2f}$")
