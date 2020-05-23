class Solution:
    def plusOne(self, digits):
        if not digits:
            return None
        output = []
        input = 0
        for i in range(len(digits)):
            input = input + digits[i] * 10 ** (len(digits) - i - 1)
        input = input + 1
        input = str(input)
        for i in range(len(input)):
            output.append(int(input[i]))
        return output

#Convert digits to interger then convert plus-oned integer back to list.
#The problem with this approach is that if the integer after conversion exceeds maximum value of integer,
#this methon will fail