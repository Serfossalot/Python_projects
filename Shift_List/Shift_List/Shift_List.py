while True:
    my_list = []
    new_list = []
    size = int(input('How big is this list? '))
    for _ in range(size):
        my_list.append(input(f'Enter item #{_ + 1}: '))
    print(my_list)
    shift = int(input('How many shifts? '))
    new_list = my_list[shift:] + my_list[:shift]
    print(new_list)
    cont = input('Do you want to continue? Y/y: ').lower()
    if cont != 'y':
        break