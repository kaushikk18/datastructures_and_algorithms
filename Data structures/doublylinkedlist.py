# Node class

"""
   _                            _       _   _
  | |                          | |     (_) | |
  | | __   __ _   _   _   ___  | |__    _  | | __
  | |/ /  / _` | | | | | / __| | '_ \  | | | |/ /
  |   <  | (_| | | |_| | \__ \ | | | | | | |   <
  |_|\_\  \__,_|  \__,_| |___/ |_| |_| |_| |_|\_\
      
"""


class Node():

    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


# linked list class
class DoublylinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data)+' --> '
            itr = itr.next

        print(dllstr)

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, None, self.head)
            self.head = node
        else:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, itr, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


if __name__ == '__main__':
    a = DoublylinkedList()
    a.insert_at_begining('3')
    a.insert_at_end('69')
    a.insert_at_end('34')
    a.insert_at_begining('12')
    print(a.get_length())
    a.print()
