fname = input("Enter file name: ") # mbox-short.txt
fn = open(fname)
count = 0
for line in fn:
    lst = list()
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        lst.append(words)
    for x in lst:
        count = count + 1
        print(x[1])
print("There were",  count, "lines in the file with From as the first word")

