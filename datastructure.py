'''
    time:2019.4.25  21.46
'''
class array(object):
    def __init__(self, size=32):
        self._size = size
        self._item = [None] * size

    def __getitem__(self, index):
        return self._item[index]

    def __setitem__(self, index, value):
        self._item[index] = value

    def __len__(self):
        return len(self._size)

    def __iter__(self):
        for i in self._item:
            yield i


# a = array(size=10)
# a[0] = 0
# a[1] = 1
# for i in a:
#     print(i)

class Node(object):
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList(object):
    def __init__(self, maxsize=32):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full error')
        node = Node(value)
        if self.tailnode == None:
            self.root.next = node
        else:
            self.tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        headnode = self.root.next
        node = Node(value)
        node.next = headnode
        self.root.next = node
        self.length += 1

    def iter_node(self):
        current = self.root.next
        while current is not self.tailnode:
            yield current
            current = current.next
        yield current

    def __iter__(self):
        for i in self.iter_node():
            yield i

    def remove(self, value):
        prenode = self.root
        current = self.root.next
        for i in self.iter_node():
            if i.val == value:
                prenode.next = i.next
                if i in self.tailnode:
                    self.tailnode = i
                del i
                self.length -= 1
                return 1
            else:
                prenode = current
        return -1

    def find(self, value):
        index = 0
        for i in self.iter_node():
            if i == value:
                return index
            index += 1
        return index

    def popleft(self):
        if self.root.next is None:
            raise Exception('This LinkedList is empty')
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        del headnode
        self.length -= 1
        return value

    def clear(self):
        for i in self.iter_node():
            del i
        self.root.next = None
        self.length = 0


# def test():
#     l = LinkedList()
#     l.append(0)
#     l.append(1)
#     l.append(2)
#     assert len(l) == 3
#     assert l[2] == 2
#     assert l[3] == -1
#
#     l.remove(0)
#     assert len(l) == 2
#     assert l.find(0) == -1
#     assert list[l] == [1, 2]
#
#     l.appendleft(0)
#     assert list[l] == [0, 1, 2]
#
#     l.popleft(0)
#     assert list[l] == [1, 2]
#
#     l.clear()
#     assert len(l) == 0
class doublequene(object):
    def __init__(self, maxsize=32):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception('this link is full')
        node = Node(val=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception('this link is full')
        node = Node(val=value)
        if self.root.next is self.root:
            self.root.next = node
            node.prev = self.root
            node.next = self.root
            self.root.prev = node
        else:
            head = self.root.next
            node.prev = self.root
            node.next = head
            head.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):
        if self.root.next is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        current = self.root.next
        while current is not self.root:
            yield current
            current = current.next
        yield current

    def __iter__(self):
        for i in self.iter_node():
            yield i.val

    def iter_node_reverse(self):
        if self.root.prev is not self.root:
            return
        current = self.root.prev
        while current is not self.root:
            yield current
            current = current.prev
        yield current


class quene(doublequene):

    def pop(self):
        if len(self) <= 0:
            raise Exception('this quene is empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) <= 0:
            raise Exception('this quene is empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value


class stack(object):
    def __init__(self):
        self.quene = quene()

    def push(self, value):
        return self.quene.append(value)

    def pop(self):
        return self.quene.pop()

    def __len__(self):
        return len(self.quene)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = stack()
    for i in range(3):
        s.push(i)
    assert len(s) == 3
    assert s.pop() == 2