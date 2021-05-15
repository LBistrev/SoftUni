items_with_price = input().split("|")
budget = float(input())
max_price_clothes = 50
max_price_shoes = 35
max_price_accessories = 20.50
list_with_increased_prices = []
bought_items_price = 0
current_item_price = 0

for item in items_with_price:
    items, price_current_item = item.split("->")
    price_current_item = float(price_current_item)
    if budget <= 0:
        break
    if items == "Clothes":
        if price_current_item > max_price_clothes:
            continue
        elif budget >= price_current_item:
            budget -= price_current_item
            bought_items_price += price_current_item
            new_price = price_current_item + price_current_item * 0.4
            current_item_price += new_price
            list_with_increased_prices.append(new_price)
        else:
            continue
    elif items == "Shoes":
        if price_current_item > max_price_shoes:
            continue
        elif budget >= price_current_item:
            budget -= price_current_item
            bought_items_price += price_current_item
            new_price = price_current_item + price_current_item * 0.4
            current_item_price += new_price
            list_with_increased_prices.append(new_price)
        else:
            continue
    elif items == "Accessories":
        if price_current_item > max_price_shoes:
            continue
        elif budget >= price_current_item:
            budget -= price_current_item
            bought_items_price += price_current_item
            new_price = price_current_item + price_current_item * 0.4
            current_item_price += new_price
            list_with_increased_prices.append(new_price)
        else:
            continue
end_sum = current_item_price + budget
final_prices = []
for current_price in list_with_increased_prices:
    final_prices.append(f"{current_price:.2f}")
print(" ".join(final_prices))
print(f"Profit: {current_item_price - bought_items_price:.2f}")

if end_sum >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

a = 5
