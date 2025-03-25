class Node:
    def __init__(self, num):
        self.value = num
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
        tba = Node(num)
        self.tail.next = tba
        tba.prev = self.tail
        self.tail = self.tail.next

    def lprint(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.value, end=" ")
            cur_node = cur_node.next
        print()

    def rprint(self):
        cur_node = self.tail
        while cur_node is not None:
            print(cur_node.value, end=" ")
            cur_node = cur_node.prev
        print()

    def insert(self, index, num):
        cur_node = self.head
        c = 0
        while c < index:
            cur_node = cur_node.next
            c += 1

        # we have to insert here at cur_node

        new_node = Node(num)
        new_node.next = cur_node
        cur_node.prev.next = new_node
        new_node.prev = cur_node.prev
        cur_node.prev = new_node


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.lprint()
    dll.rprint()
    print("after inserting 69 at 1: ")
    dll.insert(1, 69)
    dll.lprint()
