#number
a = 4.24E10 #실수 4.24 10 *10
print(a)
a = 0o177 #8진수
print(a)
a=3
b=4
print(a+b)
print(a*b)
print(a/b)
print("=" * 50)

print(a**b) # 3의 4제곱
print("=" * 50)

print(7%3) #나머지

print(7/4)
print(7//4) #몫
print("=" * 50)

#string
"Hello World"
'Python is fun'
"""Life is too short, 
You need python"""
'''Life is too short, 
You need python'''

food = "Python's favorite food is perl"
print(food)
say = '"Python is very easy." he says.'
print(say)
print("=" * 50)

multiline1 = "Life is too short\nYou need python"
multiline2='''
Life is too short
You need python
'''
print(multiline1)
print(multiline2)
print("=" * 50)

#string operator
head = "Python"
tail = " is fun!"
print(head + tail)
a = "python"
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short, You need Python"
print(a[0])
print(a[-0])
print("=" * 50)
print(a[-1])
print(a[12])

print("=" * 50)
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
'Life'
print("=" * 50)
a = "Life is too short, You need Python"
print(a[0:4])
print("=" * 50)
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
'20010331'
print(weather)
'Rainy'
print("=" * 50)
a = "Pithon"
a[:1]
'P'
a[2:]
'thon'
print(a[:1] + 'y' + a[2:])
'Python'
print("=" * 50)

number = 3
print("I eat {0} apples".format(number))
'I eat 3 apples'
print("=" * 50)

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
'I ate 10 apples. so I was sick for three days.'
print("=" * 50)
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
'I ate 10 apples. so I was sick for 3 days.'
print("=" * 50)
print("{0:<10}".format("hi"))
'hi        '
print("{0:>10}".format("hi"))
'        hi'
print("{0:^10}".format("hi"))
'    hi    '
print("{0:=^10}".format("hi"))
'====hi===='
print("{0:!<10}".format("hi"))
'hi!!!!!!!!'
print("=" * 50)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
'나의 이름은 홍길동입니다. 나이는 30입니다.'
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
'나의 이름은 홍길동입니다. 나이는 30입니다.'
print(f'{"hi":<10}')  # 왼쪽 정렬
'hi        '
print(f'{"hi":>10}')  # 오른쪽 정렬
'        hi'
print(f'{"hi":^10}')  # 가운데 정렬
'    hi    '
print("=" * 50)

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

a = "Life is too short"
print(a.index('t'))
# print(a.index('k')) #error occur
print("=" * 50)

print(" || ".join('abcd'))
'a,b,c,d'

print(",".join(['a', 'b', 'c', 'd']))
'a,b,c,d'

a = "hi"
print(a.upper())
a = "HI"
print(a.lower())
#lstring(), rstring(), strip()

a = "Life is too short"
print(a.replace("Life", "Your leg"))
print("=" * 50)
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':'))

print("=" * 50)

a = list()
print(a)

a = [1,2,3]
print(a)
print(a[0])
print(a[-1])
print(a[0] + a[2])
a.append(['a', 'b', 'c'])
print(a)
print(a[-1])
print(a[3])
print(a[-1][-1])
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[-1][-1][0])

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a)

print("=" * 50)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a*3)
a[2] = 4
print(a)
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

a = [1,2,3]
print(a.index(3))
#print(a.find(3)) #'list' object has no attribute 'find'

a = [1, 2, 3]
a.insert(0, 4)
print(len(a))

a.insert(6,10)
print(len(a))

a.remove(10)
a.sort()
a.append(1)
a.append(2)
a.append(3)
a.append(3)

print(a)
print(a.pop())
print(a)

a.extend([6,7,8])
print(a)

t2 = (1,)
print(t2)
print(type(t2))

print('='*50)

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)
a = {1: 'hi'}
print(a)
a = { 'a': [1,2,3]}
print(a)


a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())
print(list(a.keys()))

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

a.clear()
print(a)

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))


a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('nokey'))
#None
#print(a['nokey'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'nokey'

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
#True
print('email' in a)
#False

print('='*50)

s1 = set([1,2,3])
print(s1)
s2 = set("Hello")
print(s2)
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).

s1 = set([1,2,3])
l1 = list(s1)
print(l1)

print('='*50)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s2 - s1)

s1 = set([1, 2, 3])
s1.add(4)
print(s1)

s1.update([5, 6, 7])
print(s1)

s1.remove(2)
s1.remove(5)
s1.remove(7)
print(s1)

a = True
b = False

print('='*50)

if []:
    print("참")
else:
    print("거짓")
print('='*50)

if [1, 2, 3]:
    print("참")
else:
    print("거짓")
print('='*50)

print(bool('python'))
print(bool(''))
print(bool([]))

print('='*50)
a = [1,2,3]
b = a
print(id(a))
print(id(b))
a[1] = 4
print(a)
print(b)

print('='*50)

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

a = [1, 2, 3, 4, 5]
from copy import copy
b = copy(a)
a[-1] = 50

print(a)
print(b)

print('='*50)
a = b = 'python'
print(a, b)
ab = [a,b] = ['python', 'life']
print(ab)

a, b = ('python', 'life')
print(type(a))
ab = (a, b) = 'python', 'life'
print(type(ab))

print('='*50)

dic = {"국어": 80, "영어": 75, "수학":55}
total_sum = 0
for x in list(dic.values()):
  total_sum += x
print(total_sum / len(list(dic.values())))

if 13 % 2 == 0:
  print("even")
else:
  print("odd")

주민번호 = "881120-1068234"
print(주민번호.find("-"))
print(주민번호[0:6])

print(주민번호[주민번호.find("-")+1])

a = "a:b:c:d"
string = a.split(":")
print('#'.join(string))
print('='*50)

s = [1,3,5,4,2]
s.sort()
s.reverse()
print(s)

print(" ".join(['Life', 'is', 'too', 'short']))

print((1,2,3) + (4,))
print('='*50)

a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

print('='*50)

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a = set(a)
print(a)

print('='*50)

a = b = [1, 2, 3]
a[1] = 4
print(a)
print(b)