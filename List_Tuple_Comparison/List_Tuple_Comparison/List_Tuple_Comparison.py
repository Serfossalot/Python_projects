# List vs Tuple Solution
import timeit

my_list = list(range(1000000))
my_tuple = tuple(range(1000000))

def access_all_list():
    for element in my_list:
        _ = element  # Accessing each element

def access_all_tuple():
    for element in my_tuple:
        _ = element  # Accessing each element

# Measure access time
list_time = timeit.timeit(access_all_list, number=10)
tuple_time = timeit.timeit(access_all_tuple, number=10)

print(f"List access time:\t{list_time:.5f} seconds")
print(f"Tuple access time:\t{tuple_time:.5f} seconds")

