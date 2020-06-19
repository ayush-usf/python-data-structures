dict1 = {"a":1,"b":2}
dict2 = {"a":4,"c":3}
dict3 = {"a":4,"c":3}
print('dict1: ', dict1)
print('dict2: ', dict2)

print("================= Mergeing 2 dicts (Using **) - New var created =================\n")
merged_dict1 = {**dict1, **dict2}
print("The latter's values will be considered")
print('merged_dict1: {**dict1, **dict2} ', merged_dict1)  # {'a': 4, 'b': 2, 'c': 3}

merged_dict2 = {**dict2, **dict1}
print('merged_dict1: {**dict2, **dict1} ', merged_dict2)  # {'a': 1, 'c': 3, 'b': 2}

print("================= Mergeing 2 dicts (update) =================")
dict2.update(dict1)
print('dict2.update(dict1)')
print('dict2: ', dict2)

dict1.update(dict3)
print('dict1.update(dict2)')
print('dict1: ', dict1)

print("================= Print Dict (beautify) =================")
import json
print('json.dumps(dict1, indent=4): ', json.dumps(dict1, indent=4))