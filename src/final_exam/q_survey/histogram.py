def display_histogram(list1):
    
    
    for num in list1:
        print(num, end='')
        number = int(num)
        index = 0
        while index < number:
            print('*', end='')
            index += 1

        print('\n')
