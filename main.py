def changeTuple(key, value, my_tuple):
    lst = list(my_tuple)
    lst[key] = value
    my_tuple = tuple(lst)
    return my_tuple

my_tuple = ("data analyst", "data scientist", "data engineer", "data architect")
my_tuple = changeTuple(0, "test", my_tuple)
print(my_tuple)
