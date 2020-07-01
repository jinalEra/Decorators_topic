
#@property use for getter and setter its a decorator
# class Square:
#     def __init__(self,side):
#         self.side = side
#     @property
#     def side(self):
#         return self._side
#     @side.setter
#     def side(self, value):
#         if value >= 0 :
#             self._side = value
#         else:
#             print("error")
#     @property
#     def area(self):
#         return self._side **2
#     @classmethod
#     def unit_sqaure(cls):
#         return cls(1)
#
# s = Square(5)
# print(s.side)
# print(s.area)
class bank_inter:
    def __init__(self,balance):
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("error")
    @property
    def intrest(self):
        return self._balance*5/100
    @classmethod
    def unit_sqaure(cls):
        return cls(1)

b = bank_inter(100)
print(b.balance)
print(b.intrest)

