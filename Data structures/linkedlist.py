
# Node class
class Node():

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# linked list class
class LinkedList:

    def __init__(self):
        self.head_node = None

    def print(self):
        if self.head_node is None:
            print("Linked list is empty")
            return
        itr = self.head_node
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> '
            itr = itr.next

        print(llstr)

    def insert_at_begining(self, data):
        node = Node(data, self.head_node)
        self.head_node = node

    def insert_at_end(self, data):
        if self.head_node is None:
            self.head_node = Node(data, None)
            return

        itr = self.head_node

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head_node = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head_node
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head_node
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head_node = self.head_node.next
            return

        count = 0
        itr = self.head_node
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':

    ll = LinkedList()
    ll.insert_at_begining('21')
    ll.insert_at_begining('69')
    ll.insert_at_end('92')
    ll.insert_at(2, '234')
    ll.remove_at(0)
    # ll.insert_values(['kaushik', 'jeeva', 'harith'])
    # print('the length is', ll.get_length())

    ll.print()
