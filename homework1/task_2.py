class Data:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Data(value)
        else:
            q = Data(value)

            temp = self.head
            self.head = q
            self.head.next = temp

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


q = Queue()

q.push(10)
q.push(20)
q.push(30)
# s.push(4)
# s.push(5)

print(f'stack: {q}')
print(f'stack len: {len(q)}')
try:
    print(f'stack pop: {q.pop()}')
    print(f'stack: {q}')
    print(f'stack len: {len(q)}')

    print(f'stack pop: {q.pop()}')
    print(f'stack: {q}')
    print(f'stack len: {len(q)}')

    print(f'stack pop: {q.pop()}')
    print(f'stack: {q}')
    print(f'stack len: {len(q)}')

    print(f'stack pop: {q.pop()}')
    print(f'stack: {q}')
    print(f'stack len: {len(q)}')
except Exception as e:
    print(e)

# print(s.pop())
# print(s)