# class Lists:

#     def __init__(self, list1):
#         self.list1 = list1

#     def calculate(self):
#         sum = 0
#         min = self.list1[0]
#         max = self.list1[0]
#         for i in self.list1:
#             sum = sum + i
#             if i < min:
#                 min = i
#             if i > max:
#                 max = i
#         return sum, min, max


# list1 = [1, 2, 3, 4, 5]
# obj = Lists(list1)
# sum, min, max = obj.calculate()
# print("Sum:", sum)
# print("Min:", min)
# print("Max:", max)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

p1 = Person("Salome", 20)

p1.myfunc()



