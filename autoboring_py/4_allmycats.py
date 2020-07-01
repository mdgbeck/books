cat_names = []
i = 1
while True:
    print('Enter the name of cat ' + str(i) +
            ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        print("All your cats' names are: ", end = '')
        for name in cat_names:
            print(' ' + name, end = '')
        print()
        break
    cat_names = cat_names + [name]
    print('The cat names are:')
    for name in cat_names:
        print(' ' + name)
    i += 1
