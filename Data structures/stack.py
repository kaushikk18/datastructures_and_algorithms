# user defined data structure
# last in first out LIFO
# push for insertion
# pop for removal
# conditions to check - overflow, underflow


class stack:

    def __init__(self):
        self.data = []  # an empty stack is being created

    def length(self):  # method for checking the length of the list
        return len(self.data)

    def is_full(self):  # method for chcking the list is full or not
        if len(self.data) == 5:
            return True
        else:
            return False

    def push(self, element):  # method for inserting a new element in the stack(in the last)
        if len(self.data) < 5:
            self.data.append(element)
        else:
            return 'Overflow'

    def pop(self):  # method for removing a element from the stack(removing the last element)
        if len(self.data) == 0:
            return 'Underflow'
        else:
            return self.data.pop()


a = stack()  # creating a object named 'a' of the class 'stack'
a.push(23)
a.push(56)
a.push(69)
a.push(16)
a.push(78)
a.push(35)

print(a.length())
print(a.is_full())
print(a.data)
# we cant push elements anymore as the stack reached the max size. therefore 'overflow'
print(a.push(17))

print(a.pop())
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# print(a.pop())  # there us no element in the stack to remove. therefore 'underflow'
