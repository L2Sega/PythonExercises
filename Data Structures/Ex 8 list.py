fname = input("Enter file name: ") # mbox-short.txt
fn = open(fname)
count = 0
for line in fn:
    if line.startswith('From '):
        line = line.rstrip()
        words = line.split()
        if words == []: continue
        count = count + 1
        print(words[1])
print("There were",  count, "lines in the file with From as the first word")

