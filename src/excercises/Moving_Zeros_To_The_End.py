def move_zeros(array):
    zeros = []
    rest = []

    for i in array:
        if not (i is False) and i == 0:
            zeros.append(i)
        else:
            rest.append(i)

    return rest + zeros


print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros(['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, False, 0, 0, 0, 0, 0, 0, 0]))