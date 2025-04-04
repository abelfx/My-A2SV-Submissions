# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten >= 1:
                    if five >= 1:
                        ten -= 1
                        five -= 1
                    else:
                        return False
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
        