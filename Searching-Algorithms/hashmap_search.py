def buildhashmap(arr):
    h = {}
    for i in range(len(arr)):
        h[arr[i]] = i
    return h


def hashmap(target, arr):
    h = buildhashmap(arr)
    return h.get(target, -1)


print(hashmap(2, [1, 2, 3]))  # 1