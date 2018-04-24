def eliminate_different_contents(some_value):
    def map_to_one_value(i):
        if isinstance(i , list):
            return eliminate_different_contents(i)

        return 0

    if isinstance(some_value, list):
        return list(map(map_to_one_value, some_value))
    else:
        return some_value


def same_structure_as(original, original_other):
    transformed = eliminate_different_contents(original)
    other_transformed = eliminate_different_contents(original_other)

    return transformed == other_transformed


print(same_structure_as([1,[1,1]],[2,[2,2]]))
print(same_structure_as([1,[1,[3, [2]]]],[2,[2,[4, [9]]]]))
print(same_structure_as([1,[1,1]],[[2,2],2]))
