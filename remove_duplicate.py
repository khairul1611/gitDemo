array = [1, 2, 2, 3, 4, 4, 5]

unique_array = []
seen = set()

for num in array:
    if num not in seen:
        unique_array.append(num)
        seen.add(num)

print(unique_array)
