
# Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom.

# Array List has indexes and could provide Insert and GetRandom in average constant time, though has problems with Delete.

# To delete a value at arbitrary index takes linear time. The solution here is to always delete the last value:
# * Swap the element to delete with the last one.
# * Pop the last element out.


from random import choice
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)






# import random
# class RandomizedSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.random_set=[]
        

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val in self.random_set:
#             return False
#         else:
#             self.random_set.append(val)
#             return True
        

#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.random_set:
#             self.random_set.remove(val)
#             return True
#         else:
#             return False
        

#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         #print(self.random_set)
#         length = len(self.random_set)
#         #print('length',length)
#         rand_num = random.randint(0,length-1)
#         #print('rand_num',rand_num)
#         new_num = self.random_set[rand_num]
        
#         return new_num
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()