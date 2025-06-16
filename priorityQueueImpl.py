#Priority Queue Implementation by designing task class.
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

# returns the task details in a readable format.
    def __repr__(self):
        return (f"Task(id={self.task_id}, priority={self.priority}, "
                f"arrival={self.arrival_time}, deadline={self.deadline})")
    
def insert(heap, task):
    """Insert a new task into the heap and maintain the max-heap property."""
    heap.append(task)
    i = len(heap) - 1
    # Sift up to maintain heap property
    while i > 0:
        parent = (i - 1) // 2
        if heap[i].priority > heap[parent].priority:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

def extract_max(heap):
    """Remove and return the task with the highest priority from the max-heap."""
    if not heap:
        return None
    max_task = heap[0]
    last_task = heap.pop()
    if heap:
        heap[0] = last_task
        i = 0
        n = len(heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < n and heap[left].priority > heap[largest].priority:
                largest = left
            if right < n and heap[right].priority > heap[largest].priority:
                largest = right
            if largest != i:
                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest
            else:
                break
    return max_task

def increase_key(heap, index, new_priority):
    """Increase the priority of the task at 'index' and adjust its position in the max-heap."""
    if new_priority < heap[index].priority:
        raise ValueError("New priority is less than current priority.")
    heap[index].priority = new_priority
    while index > 0:
        parent = (index - 1) // 2
        if heap[index].priority > heap[parent].priority:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
        else:
            break

def decrease_key(heap, index, new_priority):
    """Decrease the priority of the task at 'index' and adjust its position in the max-heap"""
    
    if new_priority > heap[index].priority:
        raise ValueError("New priority is greater than current priority.")
    heap[index].priority = new_priority
    n = len(heap)
    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < n and heap[left].priority > heap[largest].priority:
            largest = left
        if right < n and heap[right].priority > heap[largest].priority:
            largest = right
        if largest != index:
            heap[index], heap[largest] = heap[largest], heap[index]
            index = largest
        else:
            break

def is_empty(heap):
    """Check if the heap is empty."""
    return len(heap) == 0

# Priority Queue Implementation using a Max-Heap
if __name__ == "__main__":
    heap = []

    # Adding some tasks
    insert(heap, Task(5, 7, 4, 9))
    insert(heap, Task(3, 8, 2, 8))
    insert(heap, Task(1, 5, 0, 10))
    insert(heap, Task(4, 1, 3, 15))
    insert(heap, Task(2, 3, 1, 12))  

    print("Heap after inserting tasks:")
    print(heap)

    print("\nExtracting tasks by priority:")
    while not is_empty(heap):
        task = extract_max(heap)
        print("Extracted:", task)