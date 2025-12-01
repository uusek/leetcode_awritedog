target = input('目标')
arn = list(input('').strip())

print(target, arn)

for i in range(len(arn)-1):
    if arn[i] + arn[i+1] == target:
        print(index(arn[i]), arn[i+1])
        break