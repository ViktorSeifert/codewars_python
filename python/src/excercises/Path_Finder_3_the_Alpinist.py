def path_finder(area):
    # print(area)
    area = area.split("\n")
    area = [list(map(lambda x: int(x), it)) for it in area]
    coord_sup = len(area[0])

    distances = [[float("inf")] * coord_sup for _ in range(coord_sup)]

    touched = {(0, 0)}
    distances[0][0] = 0

    while len(touched) > 0:
        current_coords = min(touched, key=lambda e: distances[e[0]][e[1]])
        touched.remove(current_coords)

        if current_coords[0] + 1 < coord_sup:
            new_coords = (current_coords[0] + 1, current_coords[1])
            update(area, current_coords, distances, new_coords, touched)

        if current_coords[1] + 1 < coord_sup:
            new_coords = (current_coords[0], current_coords[1] + 1)
            update(area, current_coords, distances, new_coords, touched)

    return distances[coord_sup - 1][coord_sup - 1]


def update(area, current_coords, distances, new_coords, touched):
    distance = abs(area[current_coords[0]][current_coords[1]]
                   - area[new_coords[0]][new_coords[1]])
    if distances[current_coords[0]][current_coords[1]] + distance \
            < distances[new_coords[0]][new_coords[1]]:
        distances[new_coords[0]][new_coords[1]] = distances[current_coords[0]][current_coords[1]] + distance
        touched.add(new_coords)


a = "\n".join([
    "000",
    "000",
    "000"
])

b = "\n".join([
    "010",
    "010",
    "010"
])

c = "\n".join([
    "010",
    "101",
    "010"
])

d = "\n".join([
    "0707",
    "7070",
    "0707",
    "7070"
])

e = "\n".join([
    "700000",
    "077770",
    "077770",
    "077770",
    "077770",
    "000007"
])

f = "\n".join([
    "777000",
    "007000",
    "007000",
    "007000",
    "007000",
    "007777"
])

g = "\n".join([
    "000000",
    "000000",
    "000000",
    "000010",
    "000109",
    "001010"
])

h = "\n".join([
    "8"
])

i = "\n".join([
    "551116",
    "222691",
    "067029",
    "053367",
    "113646",
    "652395",
])

#print(path_finder(a), 0)
#print(path_finder(b), 2)
#print(path_finder(c), 4)
#print(path_finder(d), 42)
#print(path_finder(e), 14)
#print(path_finder(f), 0)
#print(path_finder(g), 4)
#print(path_finder(h), 0)
print(path_finder(i), 14)
