num = int(input())
names = []
for _ in range(num):
    names.append(input().split())

phoneBook = {name: number for name,number in names}

for i in range(num):
    name = input()
    if name in phoneBook:
        print('%s=%s'.format(name, phoneBook[name]))
    else:
        print('Not found')
