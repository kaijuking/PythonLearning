def intersect_v1(x, y: list) -> list:
    result_list = []

    for item in x:
        if item in y:
            result_list.append(item)

    return result_list

def intersect_v2(x, y: list) -> list:
    return list(set(x).intersection(y))

def pair(x, y: list) -> list:
    for item_x in x:
        for item_y in y:
            print("{0} {1},".format(item_x, item_y))

if __name__ == "__main__":
    x = ["dog", "cat", "bird"]
    y = ["mouse", "cat", "fish"]
    v1_result = intersect_v1(x, y)
    v2_result = intersect_v2(x, y)

    print("intersect_v1 = {0}".format(v1_result))
    print("intersect_v2 = {0}".format(v2_result))

    pair(x, y)

