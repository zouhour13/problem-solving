def linear_search(arr, target)
    for i in range(len(arr))
        if arr[i] == target
            return i
    return -1


# Example usage
print(linear_search([2, 3, 9], 9))  # Output 2
print(linear_search([1, 5, 7], 4))  # Output -1