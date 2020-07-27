# result = 0

# def add(num):
#     global result
#     result += num
#     return result

# print(add(3))
# print(add(4))
# print(add(7))

#class

class Calculator:
  def __init__(self):
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result

  def sub(self, num):
    self.result -= num
    return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal2.sub(7))

print("="*50)

class Cookie:
  pass

a = Cookie()
b = Cookie()

print(a)
print(b)

print("="*50)
print("="*50)

class FourCal:
  def __init__(self, first, second):
      self.first = first
      self.second = second


  def add(self):
      result = self.first + self.second
      return result
  def mul(self):
      result = self.first * self.second
      return result
  def sub(self):
      result = self.first - self.second
      return result
  def div(self):
      result = self.first / self.second
      return result


a = FourCal(4, 2)
# a.setdata(4, 2)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a)
print(a.add())
print(a.mul())
print(a.pow())


class SafeFourCal(FourCal):
  def div(self):
    if self.second == 0:
      return 0
    else:
      return self.first / self.second

print("="*50)
a = SafeFourCal(4, 0)
print(a.div())


print("="*50)

class Family:
    lastname = "Kim"

fam = Family()
print(fam.lastname)