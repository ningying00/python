a = 'lan'
count = 0

for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            #print(a[j]>a[j+1])
            a[j], a[j + 1] = a[j + 1], a[j]
            count += 1



