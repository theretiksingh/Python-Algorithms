__author__ = 'Retik Singh'

lst = []

length = int(input("please enter size of list : "))

for num in range(length):
    num = int(input("Please enter the number : "))
    lst.append(num)

found = False

item = int(input("please enter element you want to find. : "))

for j in range(len(lst)):
    if lst[j] == item:
        found = True
        print(f'Element {lst[j]} is found at {j+1} position')
        break

if not found:
    print( f'Element {item} not found in list')
