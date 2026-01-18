array = [10, 20, 20, 30, 30, 40, 40]
final_array = []

for i in range(len(array)):
    if i == len(array) - 1:
        final_array.append(array[i])
    elif array[i] != array[i+1]:
        final_array.append(array[i])

print(final_array)