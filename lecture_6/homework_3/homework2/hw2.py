import json

with open('input.txt', 'r') as f, open('output.txt', 'w') as f2:
    ans = json.loads(f.read())
    sums = {}
    for store, items in ans.items():
        for item, quantity in items.items():
            if item in sums:
                sums[item] += quantity
            else:
                sums[item] = quantity

    json.dump(sums, f2)
