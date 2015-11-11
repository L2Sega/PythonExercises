fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    for x in words:
        if not x in lst:
            lst.append(x)

lst.sort()
print(lst)

#romeo.txt