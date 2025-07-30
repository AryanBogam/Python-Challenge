import sys

data = ["apple", "banana", "mango", "orange", "grape", "kiwi", "pineapple"]

list_memory = sys.getsizeof(data)
print(f"List memory: {list_memory} bytes")

data_tuple = tuple(data)

tuple_memory = sys.getsizeof(data_tuple)
print(f"Tuple memory: {tuple_memory} bytes")

memory_saved = list_memory - tuple_memory
print(f"Memory saved: {memory_saved} bytes")