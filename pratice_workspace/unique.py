data=['python','code','loop','if','python','else','if']
a={'if','else'}
unique=set()
for item in data:
    if item not in a:
       unique.add(item)
print(f"Unique non-stop words:{unique}")