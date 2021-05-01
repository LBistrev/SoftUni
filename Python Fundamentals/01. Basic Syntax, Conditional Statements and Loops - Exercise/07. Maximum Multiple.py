divisor = int(input())

bound = int(input())
n = 0
for num in range(1, bound + 1):
   if num % divisor == 0:
       n = num

print(n)
