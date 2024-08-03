import heapq

def merge_k_lists(lists):
    min_heap = []
    result = []

    # Ініціалізація купи: додаємо перший елемент з кожного списку
    for i, l in enumerate(lists):
        if l:  # Перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (l[0], i, 0))

    # Основний цикл
    while min_heap:
        val, list_index, element_index = heapq.heappop(min_heap)
        result.append(val)
        
        # Якщо є наступний елемент у тому ж списку, додайте його в купу
        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, list_index, element_index + 1))

    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
