fruits = {'apple': 2, 'banana': 3, 'apricot': 4, 'berry': 5}

product = 1
for key, value in fruits.items():
    if key.startswith('a'):
        product *= value

print("Product of values:", product)
