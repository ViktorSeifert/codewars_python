def get_min_climb(area, distances, coords):
    climbs = []
    if coords[0] > 0:
        climbs.append(abs(area[coords[0] - 1][coords[1]] - area[coords[0]][coords[1]])
                      + distances[coords[0] - 1][coords[1]])
    if coords[1] > 0:
        climbs.append(abs(area[coords[0]][coords[1] - 1] - area[coords[0]][coords[1]])
                      + distances[coords[0]][coords[1] - 1])

    return min(climbs)


def path_finder(area):
    area = area.split("\n")
    area = [list(map(lambda x: int(x), it)) for it in area]
    coord_sup = len(area[0])
    if coord_sup == 1:
        return area[0][0]

    distances = [[0] * coord_sup for _ in range(coord_sup)]

    finished = [(0, 0)]
    touched = [(0, 1), (1, 0)]

    while len(touched) > 0:
        current_coords = touched.pop(0)
        min_climb = get_min_climb(area, distances, current_coords)

        distances[current_coords[0]][current_coords[1]] = min_climb
        finished.append(current_coords)

        if current_coords[0] + 1 < coord_sup:
            new_coords = (current_coords[0] + 1, current_coords[1])
            if new_coords not in finished:
                touched.append(new_coords)

        if current_coords[1] + 1 < coord_sup:
            new_coords = (current_coords[0], current_coords[1] + 1)
            if new_coords not in finished:
                touched.append(new_coords)

    return distances[coord_sup - 1][coord_sup - 1]



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

print(path_finder(a), 0)
print(path_finder(b), 2)
print(path_finder(c), 4)
print(path_finder(d), 42)
print(path_finder(e), 14)
print(path_finder(f), 0)
print(path_finder(g), 4)
