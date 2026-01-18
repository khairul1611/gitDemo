# sorted

# a = input("Enter a string: ")
# b = input("Enter another sting: ")

# result = False
# for i in range(len(a)):
#     if a[i] == b[i]:
#         result = True
#     else:
#         result = False
#         break
# if result == True:
#     print("Anagam!")
# else:
#     print("Not anagam!")

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    count = {}

    for ch in str1:
        count[ch] = count.get(ch, 0) + 1

    for ch in str2:
        count[ch] = count.get(ch, 0) - 1

    for val in count.values():
        if val != 0:
            return False
    return True

print(is_anagram("rice", "rice"))