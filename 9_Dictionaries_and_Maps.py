num = int(input())
names = []

names = [input().split() for _ in range(num)]

phoneBook = {name: number for name,number in names}

while(True):
    try:
        name = input()
        if name in phoneBook:
            print(f'{name}={phoneBook[name]}')
        else:
            print('Not found')
    except:
        break
