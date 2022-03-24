class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    # Solution 1
    # def __init__(self):
    #     self.data = []

    # def add(self, number):
    #     # write your code here
    #     self.data.append(number)

    # def find(self, value):
    #     # write your code here
    #     h = {}
    #     for num in self.data:
    #         if value - num in h:
    #             return True
    #         else:
    #             h[num] = 0
    #     return False

    # Solution 2
    def __init__(self):
        self.data = {}

    def add(self, number):
        # write your code here
        if number in self.data:
            self.data[number] += 1
        else:
            self.data[number] = 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for key in self.data.keys():
            if value - key in self.data:
                return key != value - key or self.data[key] > 1
        return False