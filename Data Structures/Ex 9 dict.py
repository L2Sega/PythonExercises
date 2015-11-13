name = input("Enter file:") # mbox-short.txt
handle = open(name)
count = dict()
bigcount = None
bigmail = None

for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        count[words[1]] = count.get(words[1], 0) + 1

for a, b in count.items():
    if bigcount is None or b > bigcount:
        bigcount = b
        bigmail = a

print(bigmail, bigcount)


# print(count)



