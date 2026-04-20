import random

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
        for s in range (min_index, len(values)):
            if values [s] < min_value:
                min_int = s
                min_value = values [s]
        values [min_int], values [min_index] = values [min_index], values [min_int]
        print (values)



