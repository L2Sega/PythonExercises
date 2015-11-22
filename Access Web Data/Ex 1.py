import re
fn = open('regex_sum_185181.txt')
mlist = 0
for li in fn:
    num = re.findall('([0-9]+)', li)
    for i in num:
        mlist += int(i)
print(mlist)





