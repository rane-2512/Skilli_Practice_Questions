def findCommonElements(list1: list[int], list2: list[int]) -> list[int]:
    common = []

    for i in list1:
        if i in list2 and i not in common:
            common.append(i)

    common.sort()

    return common
