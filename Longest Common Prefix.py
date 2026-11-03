def longestCommonPrefix(str: list[str]) -> str:
    if len(str) == 0:
        return ""

    prefix = str[0]

    for i in range(1, len(str)):
        while not str[i].startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix
