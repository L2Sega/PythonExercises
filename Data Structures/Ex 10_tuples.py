# name = input("Enter file: ") # mbox-short.txt
# handle = open(name)
# tmp = dict()
# for line in handle:
#     if line.startswith('From '):
#         line = line.rstrip()
#         words = line.split()
#         time = words[5].split(":")
#         tmp[time[0]] = tmp.get(time[0], 0) + 1
#
# my_sort = sorted([(k, v) for k, v in tmp.items()])
# for k,v in my_sort:
#     print(k, v)


# lst = list()
# for k, v in tmp.items():
#     lst.append((k, v))
# print(lst)

#         tmp.append(words[5])
#
# for i in tmp:
#     x = i.split(":")
#     print(x)

a = {'a':1,'d':4,'c':3,'bbv':2}

for i in sorted(a, key=len):
    print(i, a[i])

# s = sorted([(k, v) for k, v in a.items()])
# for k, v in s:
#     print(k, v)
