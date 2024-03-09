def all_true(my_tuple):

 return all(element for element in my_tuple)


my_tuple1 = (True, True, True)
my_tuple2 = (True, False, True)


print(f"All elements True (1, 1, 1): {all_true(my_tuple1)}")
print(f"All elements True (1, 0, 1): {all_true(my_tuple2)}")