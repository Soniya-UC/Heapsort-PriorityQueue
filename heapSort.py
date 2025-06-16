import random
import time
import tracemalloc
# Heapsort implementation in Python
def heap(arr, n, i):
    """To maintain the max-heap property for subtree rooted at index i."""
    largest = i
    left = 2 * i + 1     # left child
    right = 2 * i + 2    # right child

    # if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue with heap
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)

def build_max_heap(arr):
    """making the array into a max-heap."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)

def heapsort(arr):
    """Sort the array using heap sort algorithm."""
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        heap(arr, i, 0)             # Restore heap property

def measure_performance(array, description):
    print(f"\n{description} array:")
    print("Original array :", array[:10], "..." if len(array) > 10 else "")
    tracemalloc.start()

    start_time = time.perf_counter()
    arr_copy = array.copy()
    heapsort(arr_copy)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Sorted array :  ", arr_copy[:10], "..." if len(arr_copy) > 10 else "")
    print(f"Execution time: {end_time - start_time:.8f} seconds")
    print(f"Peak memory usage: {peak / 1024:.2f} KiB")

if __name__ == "__main__":

    n = int(input("Enter the size of the array: "))

    random_array = [random.randint(1, 100) for _ in range(n)]
    measure_performance(random_array, "Randomly generated array")

    sorted_array = list(range(1, n + 1))
    measure_performance(sorted_array, "Already sorted array")

    reverse_sorted_array = list(range(n, 0, -1))
    measure_performance(reverse_sorted_array, "Reverse sorted array")
