def maxlist(l):
    largest = float('-inf')
    second = float('-inf')

    for num in l:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else None