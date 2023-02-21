#!/usr/bin/python3


def leng_of_longest_substring(s: str) -> int:
    max_value = 0
    list_values = list()

    def find_repeated_words(array, string):
        seens = {}
        for x in array:
            if string == x:
                if x not in seens:
                    seens[x] = 1
                else:
                    seens[x] += 1
            else:
                continue

        return string, seens[string]

    seen = {}

    for x in range(len(s)):
        elem = s[:x+1]
        list_values.append(elem)
        n = x+1

        value = [s[i:i+n] for i in range(0, len(s), n)]

        a, b = find_repeated_words(value, elem)
        seen[a] = b
    print(seen)
    max_value = max(seen.values())
    highest = 0
    for x in seen.keys():
        if seen[x] == max_value:
            if highest < len(x):
                highest = len(x)
        else:
            continue
    return highest


if __name__ == "__main__":
    print(leng_of_longest_substring("abcabcbb"))
    print(leng_of_longest_substring("pwwkew"))
    print(leng_of_longest_substring("bbbbb"))
