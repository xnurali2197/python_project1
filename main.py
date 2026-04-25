class AdvancedPython:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def remove_data(self, value):
        if value in self.data:
            self.data.remove(value)

    def sort_data(self):
        self.data.sort()

    def search_data(self, value):
        return value in self.data

    def display_data(self):
        print(self.data)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0


def main():
    advanced_python = AdvancedPython()
    advanced_python.add_data(10)
    advanced_python.add_data(20)
    advanced_python.add_data(30)
    advanced_python.display_data()
    advanced_python.sort_data()
    advanced_python.display_data()
    print(advanced_python.search_data(20))

    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.display()

    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack.pop())
    print(stack.is_empty())

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue.dequeue())
    print(queue.is_empty())


if __name__ == "__main__":
    main()