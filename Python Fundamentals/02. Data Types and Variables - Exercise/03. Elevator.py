import math

people = int(input())
capacity = int(input())
counter = 0

courses = math.ceil(people / capacity)

print(courses)
