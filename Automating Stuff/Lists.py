# list = ['cat', 'bat', 'rat', 'elephant']
# del list[1]
# list.remove('bat')
#list.append('dog')
# list.insert(1, 'batman')
# print(list)
# print(list.index('rat'))

#==========================================
import copy
myList = ['a', 'z', 'A', 'Z']
newList = copy.deepcopy(myList)
newList[0] = 'Sega'
print(myList)
print(newList)
# myList.sort()
# myList.sort(key=str.lower)
# print(myList)


#======================================
# for i in range(len(list)):
#     print(i)
#
# for i in list:
#     print(i)
#for i in list[len(list)-2]:
#     print(i)

# myList = list(range(1, 100, 2))
# print(myList)


# print(len(list))
# del list[0]
# list[1:3] = 'dog', 'mouse', 'monkey'
# print(list)
# #
# spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
# print(spam[0][1])