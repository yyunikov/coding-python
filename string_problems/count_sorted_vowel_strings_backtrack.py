
class Solution:

    class Vowel:
        value: str
        index: int

        def __init__(self, value, index):
            self.value = value
            self.index = index

    vowels = {
        1: "a",
        2: "e",
        3: "i",
        4: "o",
        5: "u"
    }

    def countVowelStrings(self, n: int) -> int:
        return self.countVowelStringsRecursive(n, 1)

    def countVowelStringsRecursive(self, n: int, vowel_key: int) -> int:
        if n == 0:
            return 1

        result = 0
        print(self.vowels[vowel_key], end="")
        for i in range(vowel_key, len(self.vowels) + 1):
            result += self.countVowelStringsRecursive(n - 1, i)

        print()
        return result

print(Solution().countVowelStrings(3))
