inventory = {
    'gold': 500,
    'pouch': ['film', 'tiwne', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'begroll', 'bread loaf' ],
}
inventory['pocket'] = ['seashell', 'strange', 'berry', 'lint']
print(inventory)
inventory['backpack'].remove('dagger')
print(inventory)

inventory['gold'] = 550 
print(inventory)