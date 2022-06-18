class Solution(object):
    alphabet = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or 1 < len(s) > 15:
            raise Exception("Not a valid Roman string")

        total = 0
        stacked_total = 0

        chars = [ch for ch in s]
        for (i, current_symbol) in enumerate(s):
            next_symbol = None
            if i + 1 < len(s):
                next_symbol = chars[i + 1]

            # current is complex number: few symbols - we subtract everything
            if next_symbol and self.alphabet[next_symbol] > self.alphabet[current_symbol]:
                total -= self.alphabet[current_symbol] - stacked_total
                stacked_total = 0
            # current is complex number: few same symbols - we add everything
            elif next_symbol and self.alphabet[next_symbol] == self.alphabet[current_symbol]:
                stacked_total += self.alphabet[current_symbol]
            # something in stack - add everything to the sum
            elif next_symbol and self.alphabet[next_symbol] < self.alphabet[current_symbol]:
                total += self.alphabet[current_symbol] + stacked_total
                stacked_total = 0
            else:
                stacked_total += self.alphabet[current_symbol]
                total += stacked_total

        return total
