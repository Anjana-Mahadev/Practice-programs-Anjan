#not completed
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linked_list(self):
        if self.head == None:
            print('linked list is empty')
        else:
            itr = self.head
            ll = ''
            while itr:
                ll += str(itr.data) + '-->'
                itr = itr.next
            print(ll)


my_list = linked_list()
my_list.insert_at_beginning(3)
my_list.insert_at_beginning(12)
my_list.print_linked_list()
