# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = 1
        self.lst = []
    
    def add(self, num: int) -> None:
        if num == 0:
            self.lst.clear()
            self.prefix_product = 1
        else:
            self.prefix_product *= num
            self.lst.append(self.prefix_product)

    def getProduct(self, k: int) -> int:
        n = len(self.lst)

        div = n-k
        if n >= k:
            return self.lst[n-1] // (self.lst[div - 1] if div > 0 else 1)
        else:
            return 0
        
            
           

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)