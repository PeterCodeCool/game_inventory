import csv
import sys



mylist = {'arrow': 12, 'gold coin': 45, 'rope': 13, 'ruby': 4, 'torch': 6, 'dragger': 2}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def import_inventory(mylist):
    with open('import_inventory_elements.csv') as mylist:
        reader = csv.DictReader(mylist)
        mylist = reader

def displayInventory(inventory):
    print('    ','Inventory:')
    print(' ''Count', ' ', 'Item Name' )
    print('- - - - - - - - - - -')
    item_total=0
    for k,v in mylist.items():
        print(' ',str(v)+'      '+k)
        item_total=item_total+v
    print('- - - - - - - - - - -')
    print('Total number of items: '+ str(item_total))

def addToInventory(inventory,addedItems):
    for v in addedItems:
        if v in inventory.keys():
            inventory[v]+=1
        else:
            inventory[v]=1



addToInventory(mylist,dragon_loot)
import_inventory(mylist)    
displayInventory(mylist)    

f = open('export_inventory_elements.csv', 'w')
f.write(str(mylist))
f.close()