item_no = int(input("enter the number of items:\n"))
list_items = {}
while item_no !=0:
    saveFile = open('grocery.txt','a')
    item_name = input("Enter the item name:\n")
    item_qty = input("ENTER THE ITEM Qty:\n")
    list_items[item_name] = item_qty
    saveFile.write(item_name)
    item_no -= 1
    saveFile.close()

choice = input("press 'y' to search item,else 'n'\n")
if choice == 'y':
    query = input("Enter the item name to search:\n")
    if query in open('grocery.txt').read():
        print(list_items[query])
    else:
        print("item not found")