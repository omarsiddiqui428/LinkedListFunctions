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
