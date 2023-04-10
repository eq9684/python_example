import sys

f = open('D:\sign.txt', 'w')
sys.stdout = f
print('this is an example', file=f)
