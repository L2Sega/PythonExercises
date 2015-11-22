y = [('a', 10), ('b', 1), ('c', 22)]
x = sorted([(v, k) for k, v in y])
x.sort()
print(x)
# y.sort()
# print(y)
#=======================
# names = {'sega': 2, 'mega': 1, 'ivan': 4, 'katya': 6}
# tmp = list()
# for k, v in names.items():
#      tmp.append((v, k))
#
# tmp.sort(reverse = True)
# print(tmp)
#========================================
# names = {'sega': 2, 'mega': 1, 'ivan': 4, 'katya': 6}
# a = names.items()
# tmp = list()
#
# for k, v in a:
#     tmp.append((v, k))
# tmp.sort(reverse = True)
# print(tmp)

#============================================
# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# lst = list()
# for key, val in counts.items():
#     lst.append((val, key))
# lst.sort(reverse = True)
# for val, key in lst[:10]:
#     print(key, val)

#========================================
# names = {'sega': 2, 'mega': 1, 'ivan': 4, 'katya': 6}
# x = sorted([(v, k) for k, v in names.items()])
# x.sort(reverse = True)
# print(x)
