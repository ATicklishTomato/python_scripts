import timeit
import random

def bit_counter():
    return random.randint(0, 2**64-1).bit_count()

def count_ones():
    return bin(random.randint(0, 2**64-1)).count('1')

print(f"bit_counter: {timeit.timeit(bit_counter, number=1000000)}")
print(f"count_ones: {timeit.timeit(count_ones, number=1000000)}")