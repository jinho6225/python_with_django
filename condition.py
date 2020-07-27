#if statement

money = True

if money:
    print("take a Taxi")
else:
    print("Walk")

# if condition:
#     do something
#     do something
#     ...
# else:
#     do something
#     do something
#     ...
print('='*50)

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("take a Taxi")
else:
    print("Walk")

print('='*50)
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("take out the credit card")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
print('='*50)

#while

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print(f"hit {treeHit}count")
    if treeHit == 10:
        print("broken tree")


prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: 
"""

# number = 0
# while number != 4:
#   print(prompt)
  
# number = int(input())
# print(number)
print('='*50)


# for 

# for variable in list(or tuple, string):
#     do something
#     do something
#     ...

test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)
print('='*50)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

print('='*50)

add = 0 
for i in range(1, 11): 
    add = add + i 

print(add)

print('='*50)

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
  
print(result)
print('='*50)

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)
print('='*50)
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
print('='*50)

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)
print('='*50)

num = 1
total = 0
while num < 1001:
  if num % 3 == 0:
    total +=  num
  num += 1
print(total)
print('='*50)

num = 1
while num < 7:
  print('*' * num)
  num += 1
print('='*50)

numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers]
print(result)
print('='*50)
