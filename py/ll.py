class Node:
    def __init__(self, num: int):
        self.value = num
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, num: int):
        if self.head is None:
            # the first element has arrived
            tba = Node(num)
            self.head = tba
            self.tail = tba
            return
        node = Node(num)
        self.tail.next = node
        self.tail = self.tail.next

    def lprint(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.value, end=" ")
            cur_node = cur_node.next
        print()

    def length(self):
        c = 0
        cur_node = self.head
        while cur_node is not None:
            cur_node = cur_node.next
            c += 1
        return c

    def is_circular(self):
        # find the is circular using Floyd algorithm
        tortoise = 1
        print(tortoise)


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.lprint()
    print(ll.length())
