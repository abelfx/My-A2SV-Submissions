# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars

        def can_repair_all(time):
            total_cars_r = 0
            for rank in ranks:
                cars_r = int((time / rank) ** 0.5)
                total_cars_r += cars_r
                if total_cars_r >= cars:
                    return True
            
            return False

        
        while left < right:
            mid = (left + right) // 2
            if can_repair_all(mid):
                right = mid
            else:
                left = mid + 1
        
        return left