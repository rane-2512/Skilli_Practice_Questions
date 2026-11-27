
def longestCommonPrefix(str: list[str]) -> str:
    if not str:
        return ""

    prefix = str[0]

    for word in str[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix
