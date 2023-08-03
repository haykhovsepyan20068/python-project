import time

list1 = []
try:
    col = int(input("Enter length for the list: "))
except ValueError:
    print("Enter number,not text!")
    col = int(input("Enter length for the list: "))

try:
    for i in range(col):
        list1.append(int(input("Enter number: ")))
except ValueError:
    print("Enter number,not text!")
    for i in range(col):
        list1.append(int(input("Enter number: ")))

name = input('If you choose Bubble sort, enter B. If you choose Merge sort, enter M: ')

# Functions

def bubble_sort(mas):
    start_time = time.time()
    length = len(mas)
    for running in range(length - 1):
        for i in range(length - 1):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    end = time.time()
    print("Sorted list using Bubble sort:", mas)
    end_time = time.time()
    execution_time = end_time - start_time
    # print("Время выполнения функции:", execution_time, "секунд")


def merge_sort(arr):
    start_time = time.time()
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    end_time = time.time()
    execution_time = end_time - start_time
    # print("Время выполнения функции:", execution_time, "секунд")
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        result.extend(left[left_index:])

    if right_index < len(right):
        result.extend(right[right_index:])

    return result

if name.lower() == "b":
    start_time = time.time()
    bubble_sort(list1)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Merge sort execution time is: ", execution_time)
elif name.lower() == "m":
    start_time = time.time()
    sorted_list = merge_sort(list1)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Merge sort execution time is: ", execution_time)
    print("Sorted list using Merge sort:", sorted_list)