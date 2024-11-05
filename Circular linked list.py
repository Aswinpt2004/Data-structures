class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Insert after a specific node
    def insert_after(self, key, data):
        new_node = Node(data)
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while True:
            if temp.data == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Node with data", key, "not found.")

    # Delete from the beginning
    def delete_from_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    # Delete from the end
    def delete_from_end(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            prev.next = self.head

    # Delete a specific node
    def delete(self, key):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return

        temp = self.head
        prev = None
        while temp.next != self.head and temp.data != key:
            prev = temp
            temp = temp.next

        if temp.data == key:
            prev.next = temp.next
        else:
            print("Node with data", key, "not found.")

    # Display the circular linked list
    def display(self):
        nodes = []
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while True:
            nodes.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(map(str, nodes)) + " -> (head)")


cll = CircularLinkedList()

# Insertion operations
cll.insert_at_beginning(30)
cll.append(50)
cll.insert_after(30, 40)
print("After insertion:")
cll.display()

# Deletion operations
cll.delete_from_beginning()
print("After deleting from beginning:")
cll.display()

cll.delete_from_end()
print("After deleting from end:")
cll.display()

cll.delete(40)
print("After deleting node with data 40:")
cll.display()
