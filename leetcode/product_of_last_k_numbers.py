class ProductOfNumbers:

    def __init__(self):
        self.last_zero_index = -1
        self.array = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.array.append(self.array[-1] * num)
        else:
            self.array.append(1)
            self.last_zero_index = len(self.array) - 1

    def getProduct(self, k: int) -> int:
        n = len(self.array)
        if (self.last_zero_index >= n - k):
            return 0
        # if(self.array[n-k-1]==0):
        #   return array[n-1]
        return self.array[n - 1] // self.array[n - k - 1]

p = ProductOfNumbers()
p.add(3)    # [1, 3]
p.add(0)    # [1, 3, 1] (reset)
p.add(2)    # [1, 3, 1, 2]
p.add(5)    # [1, 3, 1, 2, 10]
p.add(4)    # [1, 3, 1, 2, 10, 40]
print(p.getProduct(2))  # 5 * 4 = 20
print(p.getProduct(3))  # 2 * 5 * 4 = 40
print(p.getProduct(4))  # 0 * 2 * 5 * 4 = 0
p.add(8)    # [1, 3, 1, 2, 10, 40, 320]
print(p.getProduct(2))  # 4 * 8 = 32
