import sys

#write to file
f = open('./example.log', 'w')
sys.stdout = f
print('this is an example', file = f)

#write to console
sys.stdout = sys.__stdout__
f.close()
