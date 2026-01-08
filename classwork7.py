def item(item_list):
    for x in item_list:
        print(x)
    item_list.append("butter")
    return item_list


item_list = ["milk", "bread", "eggs"]
list(map(lambda item: print(f"Item: {item}"), item_list))

print(item(item_list))   

item_list.pop(2)        
print(item(item_list))   
