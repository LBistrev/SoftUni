array = [int(el) for el in input().split()]
new = []
command = input()
while not command == "end":
    data = command.split()
    if data[0] == "swap":
        index_1 = int(data[1])
        index_2 = int(data[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif data[0] == "multiply":
        index_1 = int(data[1])
        index_2 = int(data[2])
        num1 = array[index_1]
        num2 = array[index_2]
        num3 = num1 * num2
        array[index_1] = num3
  #      array.remove(num1)
  #      array.insert(index_1, num3)
    elif data[0] == "decrease":
        for n in range(len(array)):
            array[n] -= 1

    command = input()
print(f"{', '.join([str(num) for num in array])}")
