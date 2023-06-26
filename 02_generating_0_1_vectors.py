# CharGPT:
# def generate_bit_vectors(number):
#     if number == 0:
#         return ['']
#     else:
#         previous_vectors = generate_bit_vectors(number - 1)
#         new_vectors = []
#         for vector in previous_vectors:
#             new_vectors.append(vector + '0')
#             new_vectors.append(vector + '1')
#         return new_vectors
#
#
# number = int(input("Enter a number: "))
# bit_vectors = generate_bit_vectors(number)
# output = '\n'.join(bit_vectors)
# print(output)

def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[idx] = num
        gen01(idx + 1, vector)


n = int(input())
vector = [0] * n

gen01(0, vector)
