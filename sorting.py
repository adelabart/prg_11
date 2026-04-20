import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

def selection_sort (values):
    for min_index in range (len(values)):
        print (values)
        min_value = values [min_index]
        min_int = min_index
        for i in range (min_index, len(values)):
            if values [i] < min_value:
                min_int = i
                min_value = values [i]
        values [min_int], values [min_index] = values [min_index], values [min_int]
        print (values)

def bubble_sort (values):
    new_values = values.copy()
    print (new_values)
    n = len (new_values)
    for val in range (n - 1):
        for v in range (n - val - 1):
            if new_values[v] > new_values [v+1]:
                new_values[v], new_values [v+1] = new_values [v+1], new_values [v]
    print (new_values)
    return new_values

