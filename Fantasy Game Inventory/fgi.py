#Zawartość wora
wor = {'sznur': 1, 'zupa grzybowa': 3, 'szyszki': 7, 'jabłka': 1, 'siekiera': 1}

#funkcja wyświetla zawartość wora
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total = item_total + int(v)
    print('Total number of items: ' + str(item_total))

displayInventory(wor)