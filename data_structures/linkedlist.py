class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """ Insert a new node right next to the head """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """ Returns how many nodes found in the LinkedList """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        """
            Stops at each node to see if node has requested data
            returns a ValueError if there is none
        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


def print_collection_forward(node):
    """ Prints a collection (i.e. a group of multiple objects) fowards """
    while node:
        print node,
        node = node.next_node


def print_collection_backward(list):
    """ Prints a collection (i.e. a group of multiple objects) backwards """
    if list == None: return
    head = list
    tail = list.next_node
    print_collection_backward(tail)
    print head,

if __name__ == '__main__':

    # Create nodes
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")

    # Link nodes
    node_a.set_next(node_b)
    node_b.set_next(node_c)
    node_c.set_next(node_d)

    print_collection_forward(node_a)
    print "\n"
    print_collection_backward(node_a)