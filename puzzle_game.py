import time

print('Welcome')
time.sleep(3)
print('''Your task is to get 4 liters of water using 3-liter and 5-liter buckets.
      You can use the commands:\n
      '1. "Fill_3" and "Fill_5" to fill the corresponding bucket'
      '2. "Empty_3" and "Empty_5" to empty the corresponding bucket.
      '3. 'Refill_3_5' and 'Refill_5_3' to pour water from one bucket to another'
      'To end the game early - Stop''')
time.sleep(3)
com = input('Enter "Start" to begin')
count = 0
x_3 = 0
x_5 = 0
while x_5 >= 0:
    if x_5 == 4:
        print(f'Congratulations, you passed the game!!! Number of operations is - {count}')
        break
    com = input('Enter the commands! Good luck!')
    if com == 'Stop':
        break
    if com == 'Fill_5':
        if x_5 == 5:
            print('The bucket is already full try another command.')
        if x_5 == 0:
            count += 1
            x_5 += 5
            print('The 5-liter bucket is full')
            print(f'In the first bucket {x_3}l')
            print(f'In the second bucket {x_5}l')
        if 0 < x_5 < 5:
            count += 1
            print('Bucket added to 5L')
            x_5 = 5
            print(f'In the first bucket {x_3}l')
            print(f'In the second bucket {x_5}l')

    if com == 'Fill_3':
        if x_3 == 3:
            print('The bucket is already full try another command.')
            print('In the first bucket 3l')
        if x_3 == 0:
            count += 1
            x_3 += 3
            print('The 3 liter bucket is filled with')
            print(f'In the first bucket {x_3}l')
            print(f'In the second bucket {x_5}l')
        if 0 < x_3 < 3:
            count += 1
            print('Bucket added to 3L')
            x_3 = 3
            print('In the first bucket 3l')
            print(f'In the second bucket {x_5}l')
    if com == 'Empty_3':
        if x_3 == 0:
            print('The bucket is already empty, try another command')
            print('In the first bucket ol')
        else:
            count += 1
            x_3 = 0
            print('The 3 liter bucket is empty')
            print('In the first bucket 0l')
        print(f'In the second bucket {x_5}l')
    if com == 'Empty_5':
        print(f'In the first bucket {x_3}l')
        if x_5 == 0:
            print('The bucket is already empty, try another command')
            print('In the second bucket 0l')
        else:
            count += 1
            x_5 = 0
            print('The 5-liter bucket is empty')
            print('In the second bucket 0l')
    if com == 'Refill_3_5':
        if x_5 == 5:
            print('The second bucket is full, try another team')
        if x_3 == 0:
            print('The 3L bucket is empty - try filling it first')
        if x_3 > 0:
            count += 1
            if x_3 + x_5 <= 5:
                x_5 = x_3 + x_5
                print(f'The 5L bucket is filled to {x_3}l')
                x_3 = 0
                print('In the first bucket 0l')
                print(f'In the second bucket {x_5}l ')
            if x_3 + x_5 > 5 and x_5 != 5:
                if x_5 == 3:
                    x_3 -= 2
                    x_5 = 5
                    print(f'In the first bucket {x_3}l')
                    print('In the second bucket 5l')
                if x_5 == 4:
                    x_3 -= 1
                    x_5 = 5
                    print(f'In the first bucket {x_3}l')
                    print('In the second bucket 5l')
    if com == 'Refill_5_3':
        if x_3 == 3:
            print('The first bucket is full, try another team')
        if x_5 == 0:
            print('The 5L bucket is empty - try filling it first')
        if x_5 > 0:
            count += 1
            if x_3 + x_5 <= 3:
                x_3 = x_3 + x_5
                print(f'The 3 litre bucket is filled to {x_5}l')
                x_5 = 0
                print(f'In the first bucket {x_3}l')
                print(f'In the second bucket {x_5}l ')
            if x_3 + x_5 > 3 and x_3 != 3:
                c = 3 - x_3
                if c >= x_5:
                    x_3 = x_5 + x_3
                    x_5 = 0
                    print(f'In the first bucket {x_3}l')
                    print(f'In the second bucket {x_5}l')
                if c < x_5:
                    x_3 = 3
                    x_5 = x_5 - c
                    print(f'In the first bucket {x_3}л')
                    print(f'In the second bucket {x_5}l')

    if com != "Fill_3" and com != 'Fill_5' and com != 'Empty_3' \
            and com != 'Empty_5' and com != 'Refill_3_5' and com != 'Refill_5_3':
        print('Invalid command')
