import math


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_new(self, new):
        if self.head is None:
            self.head = new
            self.tail = new
            return
        temp = self.tail
        temp.next = new
        new.prev = temp
        self.tail = new
        new.next = None

    def delete_node(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        temp = self.head.next
        temp.prev = None

    def relocate_node(self, node):
        if node == self.tail:
            return
        if node == self.head:
            temp = self.head.next
            temp.prev = None
            self.head = temp
            self.insert_new(node)
        else:
            temp = node.prev
            temp.next = node.next
            temp2 = node.next
            temp2.prev = temp
            self.insert_new(node)

    def prints(self):
        start = self.head
        while start is not None:
            print(start.key, start.value)
            print()
            start = start.next


class LRU:
    def __init__(self, capacity):
        self.list = DoublyLinkedL()
        self.size = 0
        self.LRU = {}
        self.capacity = capacity

    def get(self, key):
        if key in self.LRU:
            self.list.relocate_node(self.LRU[key])
            return self.LRU[key]
        else:
            return -1

    def put(self, key, value):
        node = Node(key, value)
        if key not in self.LRU:
            self.LRU[key] = node
            if self.size != self.capacity:
                self.list.insert_new(node)
                self.size += 1
            else:
                self.list.delete_node()
                self.list.insert_new(node)

    def size_list(self):
        return self.size

    def max_capacity(self):
        return self.capacity

    def print_list(self):
        start = self.list.head
        while start:
            print(start.key, start.value)
            print()
            start = start.next


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return -math.inf
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return
        parent_index = (i - 1) // 2
        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()
        root = self.tree[0]
        self.tree[0] = self.tree.pop()
        self._percolate_down(0)
        return root

    def _percolate_down(self, i):
        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return
        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2
        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)


def heap_sort(a_lst):
    h = MaxHeap()
    for a in a_lst:
        h.insert(a)
    i = len(a_lst) - 1
    while not h.is_empty():
        a_lst[i] = h.extract_max()
        i -= 1


def partB(word, k):
    occurrence_list = []
    dict = {}
    # Gets number of occurrences of each word
    for i in range(len(word)):
        if word[i] in dict:
            dict[word[i]] += 1
        if word[i] not in dict:
            dict[word[i]] = 1

    # Adds number to list of occurrences
    for i in dict.values():
        occurrence_list.append(i)
    heap_sort(occurrence_list)
    print(occurrence_list)
    words_seen = set()
    count = 0

    # Gathers to put in ascending order
    mosts = []
    most = []
    for val in dict:
        if occurrence_list[0] == dict[val]:
            mosts.append(val)
            words_seen.add(val)
            count += 1

    '''while val < len(occurrence_list):
        mosts.sort()
        for biggest in range(len(mosts)):
            most.append(mosts[m])
        mosts.clear()
        for big in dict:
            if occurrence_list[big] == dict[big] and big not in words_seen'''

def main():
    # PART A
    a = Node("Nancy", 20)
    b = Node("Nancy", 10)
    q = DoublyLinkedL()
    q.insert_new(a)
    q.insert_new(b)
    q.prints()
    a = LRU(5)
    a.put("A", 2)
    a.put("B", 6)
    a.put("C", 8)
    a.print_list()

    # PART B
    h = MaxHeap()
    words = ["hello", "hi", "hello", "no", "yes", "hello"]
    partB(words, 1)

main()
