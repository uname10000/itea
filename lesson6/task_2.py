class MyDictionary:
    def __init__(self):
        self.my_dictionary = dict()

    def get(self, key):
        return self.my_dictionary[key]

    def items(self):
        list_of_items = []
        for key in self.my_dictionary:
            list_of_items.append((key, self.my_dictionary[key]))

        return list_of_items

    def keys(self):
        list_of_keys = []
        for key in self.my_dictionary:
            list_of_keys.append(key)

        return list_of_keys

    def values(self):
        list_of_values = []
        for key in self.my_dictionary:
            list_of_values.append(self.my_dictionary[key])

        return list_of_values

    def __add__(self, other):
        new_my_dict = MyDictionary()

        for key in self.my_dictionary:
            new_my_dict[key] = self.my_dictionary[key]

        print('in __add__')
        print(other['fifth'])
        for key in other:
            print(key)
            new_my_dict[key] = other[key]

        return new_my_dict

    def __setitem__(self, key, value):
        self.my_dictionary[key] = value

    def __getitem__(self, item):
        return self.my_dictionary[item]

    def __iter__(self):
        return iter(self.my_dictionary)


a = MyDictionary()
a['first'] = 'value1'
a['second'] = 'value2'
a['third'] = 'value3'

print(f'values: {a.values()}')
print(f'keys: {a.keys()}')
print(f'items: {a.items()}')
print(f'get(second): {a.get("second")}')

b = MyDictionary()
b['forth'] = 'value4'
b['fifth'] = 'value5'

c = a + b
for k, v in c.items():
    print(f'c[{k}] = {c[k]}')
