
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# DoublyLinkedList
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the start
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print("Inserted", data, " at the start")

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print(f"Inserted {data} at the end")

    # Insert between nodes
    def insert_in_between(self, target_data, data):
        temp = self.head
        while temp is not None and temp.data != target_data:
            temp = temp.next
        if temp is None:
            print(f"{target_data} not found")
            return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        print("Inserted", data, "after", "target_data")

    # Delete node at the start
    def delete_at_start(self):
        if self.head is None:
            print("List is empty. No element to delete.")
            return
        if self.head.next is None:
            print(f"Deleted {self.head.data} from the beginning.")
            self.head = None
        else:
            print(f"Deleted {self.head.data} from the beginning.")
            self.head = self.head.next
            self.head.prev = None

    # Delete node at the end
    def delete_at_end(self):
        if self.head is None:
            print("List is empty. No element to delete.")
            return
        if self.head.next is None:
            print(f"Deleted {self.head.data} from the end.")
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            print(f"Deleted {temp.data} from the end.")
            temp.prev.next = None

    # Delete node after the node
    def delete_after(self, target_data):
        temp = self.head
        while temp is not None and temp.data != target_data:
            temp = temp.next
        if temp is None or temp.next is None:
            print(f"Element after {target_data} not found or does not exist.")
            return
        to_delete = temp.next
        print(f"Deleted {to_delete.data} after {target_data}.")
        temp.next = to_delete.next
        if to_delete.next is not None:
            to_delete.next.prev = temp

    # Display the entire list
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        temp = self.head
        print("Doubly Linked List:")
        while temp is not None:
            print(temp.data, end=" <-> " if temp.next is not None else "\n")
            temp = temp.next


# checking
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert
    dll.insert_at_start(10)  # Insert at the start
    dll.insert_at_start(20)

    dll.insert_at_end(30)    # Insert at the end

    dll.insert_in_between(20, 25)  # Insert 25 after node with data 20

    dll.display()

    # Delete
    dll.delete_at_start()  # Delete at the start
    dll.display()

    dll.delete_at_end()  # Delete node at the end
    dll.display()

    dll.delete_after(20)  # Delete node after the node with data 20
    dll.display()
