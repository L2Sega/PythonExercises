names = {'sega': 2, 'mega': 1, 'ivan': 4, 'katya': 6}
x = sorted([(v, k) for k, v in names.items()])
print(x)

# names = {'sega': 2, 'mega': 1, 'ivan': 4, 'katya': 6}
# for a, b in names.items():
#     print(a, b)

# ============================================================
# names = {'sega': 2, 'mega': 1, 'ivan': 4, 'katya': 6}
# print(list(names))
# print(names.keys())
# print(names.values())
# print(names.items())

#=============================================================
# names = {'sega': 2, 'mega': 1, 'ivan': 4, 'katya': 6}
# for key in names:
#     print(key, names[key])
#
# print('sega' in names)
# ============================================================
# counts = dict()
# names = ['sega', 'mega', 'ivan', 'sega', 'katya', 'katya']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

#=======================================================
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)
#=====================================================
# purse = dict()
# purse['candy'] = 12
# purse['apples'] = 15
# purse['rise'] = 8
# purse['rise'] = purse['rise'] + 2
# print(purse)

# names = {'sega': 2, 'mega': 1, 'ivan': 4, 'katya': 6}
# names['vova'] = 4
# print(names)
# =======================================================
# counts = dict()
# names = ['sega', 'mega', 'ivan', 'sega', 'katya', 'katya']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)