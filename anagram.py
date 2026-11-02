def anagram(n1: int, n2: int) -> bool:
    return sorted(str(n1)) == sorted(str(n2))


print(anagram(1221, 1212))  # True
print(anagram(123, 321))    # True
print(anagram(123, 112))    # False
print(anagram(0, 0))        # True
