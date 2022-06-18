class Solution:

    def longestPalindrome(self, s: str) -> str:
        palindromes = set()
        str_len = len(s)

        if str_len == 1:
            return s

        if str_len < 1 or str_len > 1000:
            return None

        longest_palindrome = None
        longest_palindrome_len = 0
        for i in range(0, str_len):
            for j in range(i, str_len + 1):
                sub_str_len = j - i
                larger_than_longest = sub_str_len > longest_palindrome_len if longest_palindrome else True

                # avoid shorter strings re-computation
                if longest_palindrome_len and not larger_than_longest:
                    continue

                sub_str = s[i:j]

                # avoid re-computation of the same ones
                if sub_str in palindromes:
                    continue

                reversed_sub_str = sub_str[::-1]
                if sub_str == reversed_sub_str:  # is palindrome
                    if not longest_palindrome or larger_than_longest:
                        longest_palindrome = sub_str
                        longest_palindrome_len = sub_str_len
                        palindromes.add(sub_str)

        return longest_palindrome
