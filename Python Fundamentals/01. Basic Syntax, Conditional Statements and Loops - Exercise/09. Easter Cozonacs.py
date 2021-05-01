budget = float(input())
price_for_flour = float(input())

price_of_eggs = price_for_flour * 0.75
price_of_milk = (price_for_flour + price_for_flour * 0.25) / 4
price_for_cozonak = price_for_flour + price_of_eggs + price_of_milk
cozonak_count = 0
colored_eggs = 0
lost_eggs = 0
while budget >= price_for_cozonak:
    cozonak_count += 1
    colored_eggs += 3
    budget -= price_for_cozonak
    if cozonak_count % 3 == 0:
        lost_eggs = cozonak_count - 2
        colored_eggs -= lost_eggs

print(f"You made {cozonak_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
