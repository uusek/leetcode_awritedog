target = input('目标')
arn = list(input('').strip())

for i in range(len(arn)):
    for j in range(i+1, len(arn)):
        if int(arn[i]) + int(arn[j]) == int(target):
            print(i, j)
            break