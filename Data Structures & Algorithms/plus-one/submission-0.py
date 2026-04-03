class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = ""
        for i in range(len(digits)):
            number += str(digits[i])
        number = int(number) + 1
        return [int(x) for x in str(number)]