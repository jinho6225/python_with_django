try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

try:
    print(4/0)
    a = [1,2,3]
    print(a[4])

except (ZeroDivisionError, IndexError) as e:
    print(e)


try:
    a = [1,2,3]
    print(a[4])
    print(4/0)

except ZeroDivisionError as e:
    print(e)
except IndexError as er:
    print(er)
