class MyList:
    def __init__(self):
        self.my_list = []

    def pop(self):
        return self.my_list.pop()

    def append(self, value):
        self.my_list.append(value)

    def insert(self, key, value):
        self.my_list.append(self.my_list[-1])
        # shift elements to right from key
        for i in range(len(self.my_list) - 2, key, -1):
            self.my_list[i] = self.my_list[i - 1]

        self.my_list[key] = value

    def remove(self, key):
        for i in range(key, len(self.my_list) - 1):
            self.my_list[i] = self.my_list[i + 1]

        del self.my_list[-1]

    def clear(self):
        # self.my_list.clear()
        for i in range(len(self.my_list) - 1, -1, -1):
            del self.my_list[i]

    def __add__(self, other):
        new_list = MyList()
        for i in self.my_list:
            new_list.append(i)

        for i in other:
            new_list.append(i)

        return new_list

    def __setitem__(self, key, value):
        self.my_list[key] = value

    def __getitem__(self, item):
        return self.my_list[item]

    def __str__(self):
        string = ''

        for i in self.my_list:
            string = string + str(i) + ' '

        return string


a = MyList()
b = MyList()

a.append(10)
a.append(20)
a.append('text1')

b.append('text2')
b.append('text3')
b.append('text4')
b.append(10.0)

print(f'List a: {a}')
print(f'List b: {b}')

c = a + b + a

print(f'List c ( a + b + a ): {c}')

b.insert(2, 400)
print(f'List b, insert b[2]=400: {b}')

b.remove(3)
print(f'List b remove 3 element: {b}')

print(f'List a pop(): {a.pop()}')
print(f'List a: {a}')

a.clear()
print(f'List a clear list: {a}')