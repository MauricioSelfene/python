from functools import reduce

my_list_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_filter = list(filter(lambda x: x%2 != 0, my_list_filter))

print(odd_filter)


my_list_map = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_map = list(map(lambda x: x**2, my_list_map))

print(odd_map)

# Se debe importar functools reduce
my_list_reduce = [2 ,2 ,2 ,2 ,2]
odd_reduce = reduce(lambda a , b: a * b, my_list_reduce)

print(odd_reduce)