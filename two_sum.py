array = [10, 20, 50, 40, 30]
array.sort()   # O(n log n) → [10, 20, 30, 40, 50]

def two_sum_pointer(target):
    front = 0
    end = len(array) - 1

    while front < end:
        current_sum = array[front] + array[end]

        if current_sum < target:
            front += 1
        elif current_sum > target:
            end -= 1
        else:
            return (front, end)

    return None


print(two_sum_pointer(90))
