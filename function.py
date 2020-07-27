#function

print("="*50)
# def name(params):
#     do something1
#     do something2
#     ...

def add(a, b): 
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)
print("="*50)

def add(a, b):
    return a+b

result = add(a=3, b=7)  # a에 3, b에 7을 전달
print(result)
print("="*50)

# def name(*params):
#     do something1
#     do something2
#     ...

def add_many(*args): 
    result = 0 
    for i in args: 
        result = result + i 
    return result 

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
print("="*50)

def print_kwargs(**kwargs):
    return (kwargs)

print(print_kwargs(a=1))
print(print_kwargs(name='foo', age=3))

print("="*50)

#lambda
add = lambda a, b: a+b
result = add(3, 4)
print(result)

# a = input()
# print(a)

# number = input("input the number: ")
# print(number)

# f = open('new.txt','w')
# for i in range(1, 11):
#   data = f"line no.{i}\n"
#   f.write(data)
# f.close()

# f = open("new.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open("new.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

f = open("new.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("new.txt",'a')
for i in range(11, 20):
    data = f"line no.{i}\n"
    f.write(data)
f.close()

f = open("new.txt", 'r')
data = f.read()
print(data)
f.close()

print("="*50)

import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

# a = input('\n what is you name?')
print("="*50)

print(f"your name is {a}")


print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))