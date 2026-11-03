def roundToNearest(s: str) -> str:
    last = int(s[-1])

    if last <= 5:
        return s[:-1] + "0"

    num = list(s[:-1])
    i = len(num) - 1

    while i >= 0 and num[i] == '9':
        num[i] = '0'
        i -= 1

    if i < 0:
        num.insert(0, '1')
    else:
        num[i] = str(int(num[i]) + 1)

    return "".join(num) + "0"
