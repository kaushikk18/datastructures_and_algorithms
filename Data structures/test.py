class stack:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def is_full(self):
        if len(self.data) == 5:
            return True
        else:
            return False

    def push(self, ele):
        if len(self.data) < 5:
            self.data.append(ele)
        else:
            return 'Overflow'

    def pop(self):
        if len(self.data) == 0:
            return 'Underflow'
        else:
            self.data.pop()


a = stack()  # creating a object named 'a' of the class 'stack'
a.push(23)
a.push(56)
a.push(69)
a.push(16)
a.push(78)
a.push(35)
print(a.data)
print(a.push(17))
print(a.pop())

# print(a.pop())


# print(a.length())
# print(a.is_full())

# print(a.push(17))

# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
