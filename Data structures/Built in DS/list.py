names = ['kaushik', 'jeeva', 'harith', 'kiran', 'mike', 'rob']

print(names)

print(names[1])  # accessing values using index value

print(names[1:3])  # slicing

names[4] = 'kumar'
print('the modified names list is ', names)

new_array = '\n'.join(names)  # join function
print(new_array)

names.append('mo')  # adding a new element in the list
names.pop(1)  # removes the value at the given index
print(names)
