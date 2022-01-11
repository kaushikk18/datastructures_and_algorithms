# user defined data structure
# first in first out FIFO
# two ends - front and rear
# two operations - 'enqueue' for inserting(done at rear) and 'dequeue' for deleting an element(done at front)
# two operations - overflow and underflow

class queue:

    def __init__(self):
        self.data = []  # an empty queue is being created

    def length(self):  # method for checking the length of the list
        return len(self.data)

    def enqueue(self, element):  # method for inserting a new element in the queue(in the last)
        if len(self.data) < 3:
            return self.data.append(element)
        else:
            return 'Overflow'

    def dequeue(self):  # method for deleting a element from the queue(removing the first element)
        if len(self.data) == 0:
            return 'Underflow'
        else:
            return self.data.pop(0)


a = queue()  # creating a object named 'a' of the class 'queue'
a.enqueue(33)
a.enqueue(45)
a.enqueue(90)
print(a.length())
print(a.data)
print(a.enqueue(17))
a.dequeue()
a.dequeue()
a.dequeue()

print(a.dequeue())
