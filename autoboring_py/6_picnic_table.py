def print_picnic(items_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '='))
    for i, j in items_dict.items():
        print(i.ljust(left_width, '.') + str(j).rjust(right_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies':10}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)
