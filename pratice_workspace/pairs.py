inform = {'name': 'Alice', 'city': 'New York', 'hobby': 'coding'}

for key, value in inform.items():
    if len(value) > 5:
        print(f"{key}: {value.upper()}")
    else:
        print(f"{key}: {value.lower()}")



