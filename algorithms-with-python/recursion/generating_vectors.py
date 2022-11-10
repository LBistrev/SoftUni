def generate_vectors(idx, vector):
    vectors_num = 2
    if idx >= len(vector):
        # print(''.join([str(x) for x in vector]))
        print(*vector, sep='')
        return
    for num in range(vectors_num):
        vector[idx] = num
        generate_vectors(idx + 1, vector)


number = int(input())

vector = [0] * number

generate_vectors(0, vector)
