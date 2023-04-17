dictionary = {'george': 16, 'amber': 19, 'gani': 23, 'bore' : 24}
search_age = [24,23]
for name,age in dictionary.items():
    for search1 in search_age:
        if search1 == age:
            print (name)