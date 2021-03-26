__author__ = 'Retik Singh'

lst = []

sentinel_value = int(input('Please enter a number'))

index = 0

size = int(input('Please enter size for list'))

for j in range(size):
    num = int(input('Please enter element for list'))
    lst.append(num)

lst.append(sentinel_value)

while True:
    if lst[index] == sentinel_value:
        print(f'{lst[index]} at position {index}')
        break
    else:
        index = index + 1
