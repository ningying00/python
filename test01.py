alist = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]
i = 0
while i < len(alist):
    if alist[i] == 1:
        alist.pop(i)
        i = i - 1
    i = i + 1
print(alist)
