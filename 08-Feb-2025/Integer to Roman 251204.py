# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        while (num >= 1):
            if(num >= 1000):
                num -= 1000
                result += "M"
                continue
            elif(num <= 1000 and num >= 900):
                num -= 900
                result += "CM"
                continue
            elif(num >= 500):
                num -= 500
                result += "D"
                continue
            elif(num <= 500 and num >= 400):
                num -= 400
                result += "CD"
                continue
            elif(num >= 100):
                num -= 100
                result += "C"
                continue
            elif (num <= 100 and num >= 90):
                num -= 90
                result += "XC"
                continue
            elif(num >= 50):
                num -= 50
                result += "L"
                continue
            elif(num <= 50 and num >= 40):
                num -= 40
                result += "XL"
                continue
            elif(num >= 10):
                num -= 10
                result += "X"
                continue
            elif(num <= 10 and num >= 9):
                num -= 9
                result += "IX"
                continue
            elif(num >= 5):
                num -= 5
                result += "V"
                continue
            elif (num <= 5 and num >= 4):
                num -= 4
                result += "IV"
                continue
            elif (num >= 1):
                num -= 1
                result += "I"

        return result


        