def split_in_two(n):
    split = len(n)//2
    return (n[:split], n[split:])

def merge_sorted(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if len(left) == i:
        result.extend(right[j:])
    else:
        result.extend(left[i:])

    return result

def merge_sort(ns):
    if len(ns) <= 1:
        return ns
    left, right = split_in_two(ns)
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge_sorted(left_sorted, right_sorted)
