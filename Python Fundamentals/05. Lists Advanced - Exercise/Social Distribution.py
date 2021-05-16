population = [int(num) for num in input().split(", ")]
wealth = int(input())

to_give = 0
is_valid = True
for el in range(len(population)):
    max_wealth = max(population)
    index_max = population.index(max_wealth)
    if population[el] < wealth:
        if population[index_max] <= wealth:
            print("No equal distribution possible")
            is_valid = False
            break
        else:
            to_give = wealth - population[el]
            population[el] += to_give
            population[index_max] -= to_give
if is_valid:
    print(population)
