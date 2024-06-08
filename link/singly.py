# Python programs to show linked list operations   
  
# Creating a node class  
class Node:  
    def __init__(self, value):  
        self.value = value  
        self.next = None  
  
# Creating a linked list class  
class Linked_List:  
    def __init__(self):  
        self.head = None  
  
    # Inserting a node at the beginning of the list  
    def insertInBeginning(self, value):  
        insertion_node = Node(value)  
        insertion_node.next = self.head  
        self.head = insertion_node  
  
    # Inserting a node after a particular node  
    def insertAfterNode(self, previous_node, value):  
        if previous_node is None:  
            print("There is no previous node. Make a new head.")  
            return  
  
        insertion_node = Node(value)  
        insertion_node.next = previous_node.next  
        previous_node.next = insertion_node  
  
    # Inserting the node at the end of the list  
    def insertInEnd(self, value):  
        insertion_node = Node(value)  
  
        if self.head is None:  
            self.head = insertion_node  
            return  
  
        last_node = self.head  
        while (last_node.next):  
            last_node = last_node.next  
  
        last_node.next = insertion_node  
  
    # Deleting a particular node   
    def deleteANode(self, pos):  
  
        if self.head is None:  
            return  
  
        temporary = self.head  
  
        if pos == 0:  
            self.head = temporary.next  
            temporary = None  
            return  
  
        # Finding the key which is to be deleted  
        for i in range(pos - 1):  
            temporary = temporary.next  
            if temporary is None:  
                break  
  
        # If the key is not in the list  
        if temporary is None:  
            return  
  
        if temporary.next is None:  
            return  
  
        next_ = temporary.next.next  
  
        temporary.next = None  
  
        temporary.next = next_  
  
    # Searching an element in the list  
    def search(self, key):  
  
        current_node = self.head  
  
        while current_node is not None:  
            if current_node.value == key:  
                return True  
  
            current_node = current_node.next  
  
        return False  
  
    # Sorting the linked list  
    def sortList(self, head):  
        current_node = head  
        index_node = Node(None)  
  
        if head is None:  
            return  
        else:  
            while current_node is not None:  
                index_node = current_node.next  
  
                while index_node is not None:  
                    if current_node.value > index_node.value:  
                        current_node.value, index_node.value = index_node.value, current_node.value  
  
                    index_node = index_node.next  
                current_node = current_node.next  
  
    # Printing the linked list  
    def printLinkedList(self):  
        temporary = self.head  
        while (temporary):  
            print(str(temporary.value) + " ", end = "")  
            temporary = temporary.next  
  
  
if __name__ == '__main__':  
  
    listt = Linked_List()  
    listt.insertInEnd(7)  
    listt.insertInBeginning(4)  
    listt.insertInBeginning(9)  
    listt.insertInEnd(2)  
    listt.insertAfterNode(listt.head.next, 8)  
  
    print('Linked list:')  
    listt.printLinkedList()  
  
    print("\nAfter deleting a node:")  
    listt.deleteANode(2)  
    listt.printLinkedList()  
  
    value_to_find = 4  
    if listt.search(value_to_find):  
        print("\n", value_to_find, "is found in the list")  
    else:  
        print("\n", value_to_find, " is not found in the list")  
  
    listt.sortList(listt.head)  
    print("Sorted Linked List: ")  
    listt.printLinkedList()  