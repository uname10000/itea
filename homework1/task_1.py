class Data:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Data(value)
        else:
            elem = self.head

            while elem is not None:
                if elem.next is None:
                    elem.next = Data(value)
                    break
                elem = elem.next

    def pop(self):
        if self.head is None:
            raise Exception('Stack is empty')

        elem = self.head
        prev_elem = None
        buf = None
        while elem is not None:
            if elem.next is None:
                buf = elem.value
                if prev_elem is not None:
                    prev_elem.next = None
                else: # stack contain only one element ( head )
                    self.head = None
                break

            prev_elem = elem
            elem = elem.next

        return buf

    def __str__(self):
        text = ''
        elem = self.head

        if elem is None:
            return ''

        while elem is not None:
            text += str(elem.value) + ' '
            elem = elem.next

        return text

    def __len__(self):
        if self.head is None:
            return 0

        elem = self.head
        count = 1

        while elem is not None:
            if elem.next is None:
                break
            count += 1
            elem = elem.next

        return count


s = Stack()

s.push(10)
s.push(20)
s.push(30)
# s.push(4)
# s.push(5)

print(f'stack: {s}')
print(f'stack len: {len(s)}')
try:
    print(f'stack pop: {s.pop()}')
    print(f'stack: {s}')
    print(f'stack len: {len(s)}')

    print(f'stack pop: {s.pop()}')
    print(f'stack: {s}')
    print(f'stack len: {len(s)}')

    print(f'stack pop: {s.pop()}')
    print(f'stack: {s}')
    print(f'stack len: {len(s)}')

    print(f'stack pop: {s.pop()}')
    print(f'stack: {s}')
    print(f'stack len: {len(s)}')
except Exception as e:
    print(e)

# print(s.pop())
# print(s)