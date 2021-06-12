numbers = [int(x) for x in input().split()]

negative_numbers = filter(lambda num: num < 0, numbers)
sum_negative = sum(negative_numbers)
print(sum_negative)

positive_numbers = filter(lambda num: num >= 0, numbers)
sum_positive =(sum(positive_numbers))
print(sum_positive)

if sum_positive > abs(sum_negative):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
