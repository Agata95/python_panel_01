# Day 03 Challenge
# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update
# update the inventory with new materials
# return in correct format, sorted alphabetically


def change_to_dict(list_to_dict):
    new_dict = {}
    for element in list_to_dict:
        new_dict[f'{element[1]}'] = element[0]

    return new_dict


def sort_dict(dict_to_sort):
    return sorted(dict_to_sort.items())


def update_inventory(current, fresh):
    inventory_dict = change_to_dict(current)
    fresh_dict = change_to_dict(fresh)

    for key, value in fresh_dict.items():
        if key in inventory_dict.keys():
            inventory_dict[key] += fresh_dict[key]
        else:
            inventory_dict[key] = value

    inventory_dict = sort_dict(inventory_dict)
    inventory_dict = list((y, x) for x, y in inventory_dict)
    results = [list(el) for el in inventory_dict]

    return results


if __name__ == '__main__':
    current_inventory = [
        [21, "Bowling Ball"],
        [2, "Dirty Sock"],
        [1, "Hair Pin"],
        [5, "Microphone"]
    ]

    fresh_delivery = [
        [2, "Hair Pin"],
        [3, "Half-Eaten Apple"],
        [67, "Bowling Ball"],
        [7, "Toothpaste"]
    ]

    reference = [
        [88, "Bowling Ball"],
        [2, "Dirty Sock"],
        [3, "Hair Pin"],
        [3, "Half-Eaten Apple"],
        [5, "Microphone"],
        [7, "Toothpaste"]]

    assert (update_inventory(current_inventory, fresh_delivery) == reference)
    print('Test 01 - ok!')
