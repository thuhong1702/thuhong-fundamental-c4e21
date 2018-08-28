inventory = {
    'gold': 500, 
    'pouch': ['flint', 'tiwne', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'break loaf'], 
}


inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].remove("dagger")
inventory['gold'] += 50
print(inventory)
