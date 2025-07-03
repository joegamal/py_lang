# data strucuters in py


# list (array, stack, queue)

my_list = []

print(type(my_list))

my_list.append(1)

my_list.insert(5,66)

print(my_list)


#tuple

my_tuple = (5,)


print(type(my_tuple))

#set in python
# set is unordered 
# set is mutable 
# no dublicates

my_set = set(my_list)

my_set = {1, 4, 5, 8}

my_set.add(888)
my_set.pop()
my_set.remove(5)
my_set.add(5)

print(type(my_set))

print(my_set)
