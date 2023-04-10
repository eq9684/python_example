import sys

f = open('./example.log', 'w')
sys.stdout = f
print('this is an example', file = f)
f.close()
