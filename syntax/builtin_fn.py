#abs
a = abs(-3)
print(a)

#all
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all([]))

#any
print(any([1, 2, 3]))
print(any([1, 2, 3, 0]))
print(any([]))

#chr
print(chr(97))
print(chr(48))

#dir
print(dir([1, 2, 3]), "list")
print(dir({'1':'a'}), "dic")

#divmod
print(divmod(7, 3))
print(7//3)
print(7%3)

#enumerate
name = "jinho"
for i, letter in enumerate(name):
  print(i, letter)

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

#filter
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

#int
print(int('3'))
#3
print(int(3.4))
#3

#len
print(len("python"))
#6
print(len([1,2,3]))
#3
print(len((1, 'a')))
#2

#list
print(list("python"))
#['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3)))
#[1, 2, 3]

#map
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times(x): 
    return x*2
print(list(map(two_times, [1, 2, 3, 4])))
print(list(map(lambda x: x*2, [1, 2, 3, 4])))


#max
print(max([1, 2, 3]))

#min
print(min([1, 2, 3]))

#ord
print(ord('a'))
#97
print(ord('0'))
#48

#pow
print(pow(2, 4))
#16
print(pow(3, 3))
#27

#range
print(list(range(5)))
print(list(range(5, 10)))

print(list(range(1, 10, 2)))
#[1, 3, 5, 7, 9]
print(list(range(0, -10, -1)))
#[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

#round
print(round(4.6))
#5
print(round(4.2))
#4

print(round(5.678, 2))

#5.68

#sorted
print(sorted([3, 1, 2]))
#[1, 2, 3]
print(sorted(['a', 'c', 'b']))
#['a', 'b', 'c']
print(sorted("zero"))
#['e', 'o', 'r', 'z']
print(sorted((3, 2, 1)))
#[1, 2, 3]

#str
print(str(3))
'3'
print(str('hi'))
'hi'
print(str('hi'.upper()))
'HI'

#sum
print(sum([1,2,3]))
#6
print(sum((4,5,6)))
#15