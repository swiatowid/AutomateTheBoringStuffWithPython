#funkcja dodaje elementy listy do słownika
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    return inventory #Bardzo ważne, że funkcja musi COŚ zwrócić

#funkcja wyświetla zawartość wora
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total = item_total + int(v)
    print('Total number of items: ' + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)