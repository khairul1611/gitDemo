ar = [2, 3, 1, 4, 5, 6, 7, 2]

def two_sum(target):
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            a = ar[i]
            b = ar[j]

            if a + b == target:
                return (i, j)

    return None   # যদি কোনো pair না পাওয়া যায়

print(two_sum(20))
