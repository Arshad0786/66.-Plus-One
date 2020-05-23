class Solution:
    def plusOne(self, digits):
        length = len(digits)
        i = length - 1
        while(i >= 0):
            if(digits[i] < 9):
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0
            i = i - 1
        digits = []
        digits.append(1)
        for i in range(length):
            digits.append(0)
        return digits

# If the digits won't carry after plus one, that means we can return it already.
# But if it keeps carring til the end, it means all element in it was 9,
# so we just carry them all. For instance : [9,9,9,9] -> [1,0,0,0,0]
