import sys
print(sys.argv)
print(sys.path)

import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

import os
f = os.popen("dir")
print(f.read())

import calendar
print(calendar.prmonth(2015, 12))