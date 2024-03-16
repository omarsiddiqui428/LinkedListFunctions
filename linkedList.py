class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    #to add a new node with "data" to the end of the linked list
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur =  self.head
        total = -1 #I'm doing this since we do not want to count the head node as it has no data. Alternatively you can start the count at 0 and say while cur.next != None
        while cur != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head #this is just what you do with linked lists to start at the beginning
        while cur_node.next != None: #while not at the las
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index > (self.length() -1) or index < 0:
            print("Error: Index entered out of range!")
            return None
        cur_idx = -1 #this makes more sense to me, starting head at -1, so index 0 is the first node containing data in the linked list, technically the second node
        cur_node = self.head
        while cur_node != None:
            cur_idx += 1
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data

    def erase(self,index):
        if index > (self.length()-1) or index < 0:
            print("Error: Index entered out of range!")
            return None
        cur_idx = -1  # this makes more sense to me, starting head at -1, so index 0 is the first node containing data in the linked list, technically the second node
        cur_node = self.head
        while cur_node != None:
            prev_node = cur_node
            cur_idx += 1
            cur_node = cur_node.next
            if cur_idx == index:
                prev_node.next = cur_node.next #cur.node will be deleted
                return

    def insert(self,index,data):
        if index > (self.length() -1):
            print("To add an element to the end of the list, use the append function instead")
            return None
        if index < 0:
            print("Error: index entered out of range!")
            return None
        cur_idx = -1
        cur_node = self.head
        while cur_node != None:
            prev_node = cur_node
            cur_node = cur_node.next
            cur_idx += 1
            if cur_idx == index:
                new_node = node(data)
                prev_node.next = new_node
                new_node.next = cur_node
                return

#testing inputs

my_list = linked_list()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.insert(1,'song')
my_list.display()


# The two classes here are "node" and "linked_list" . The __init__ method is the constructor that initalizes the node with optional data and 'next' pointer set to "None" by default. This allows us to access instance variables self.data and self.next within the class method. 

# The linked_list class represents a linked list 

# Classes give you access to instance variables that you can define 

# How classes benefit the code above (in simple terms):
# * 		Organizing Related Functions and Data:
#     * Classes help in organizing related functions and data together. In the provided code, the node class defines the structure of a node in a linked list, including its data (self.data) and a pointer to the next node (self.next). This encapsulation of data and functions related to nodes helps in maintaining a clear and organized structure.
# * 		Encapsulation and Modularity:
#     * Classes provide encapsulation, which means they bundle data (variables) and functions (methods) that operate on that data together. This helps in keeping the implementation details of a data structure (like a linked list) hidden and only exposing the necessary interfaces to the outside world. For example, users of the linked list don't need to know how nodes are implemented; they only need to interact with methods like append, length, display, etc.
# * 		Code Reusability:
#     * Classes promote code reusability by allowing you to create multiple instances of the same class with different data. For example, you can create multiple linked lists using the linked_list class, each with its own set of nodes and data.
# * 		Abstraction:
#     * Classes help in abstraction by hiding complex implementation details and providing a simpler interface. For example, the linked_list class abstracts away the complexities of managing pointers and nodes in a linked list. Users can interact with the linked list using high-level methods like append, length, display, etc., without worrying about low-level details.
# * 		Maintenance and Scalability:
#     * Using classes makes code maintenance easier and promotes scalability. If you want to add new features or modify existing functionalities, you can do so within the class without affecting other parts of the code. This modular approach makes it easier to manage and extend the codebase over time.
# In simple terms, classes in this code make it easier to work with linked lists by organizing related functionalities and data, promoting code reusability, hiding implementation details, and providing a clear and structured way to interact with the data structure. While functions could be used to achieve similar functionality, using classes adds a layer of abstraction and organization that makes the code more maintainable, scalable, and easier to understand.



