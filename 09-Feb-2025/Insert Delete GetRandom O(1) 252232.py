# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.numsList = []
        self.dict = {}
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.numsList)
        self.numsList.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.dict:
            indx = self.dict[val]
            lst_val = self.numsList[-1]

            self.numsList[indx] = lst_val
            self.dict[lst_val] = indx

            self.numsList.pop()
            del self.dict[val]
            return True    
        return False

        

    def getRandom(self) -> int:
        return random.choice(self.numsList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()