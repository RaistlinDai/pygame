import array
test1 = {'F1':{1:'A', 2:'B'}}
key1 = 'X'

test1['F1'][3] = 'C'

print(test1)

test2 = [1,2,3]
test3 = [4,5]

if isinstance(test2, list):
    print('YES')

for item in test3:
    test2.append(item)
print(test2)