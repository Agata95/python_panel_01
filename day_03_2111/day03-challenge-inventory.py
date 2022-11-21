# Day 03 Challenge
# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update
# update the inventory with new materials
# return in correct format, sorted alphabetically

def update_inventory(current_inventory, fresh_delivery):
    # put your logic here
    return current_inventory


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
    assert(update_inventory(current_inventory, fresh_delivery) == reference)
    print('Test 01 - ok!')
