import heapq

def minimum_cost_to_connect_cables(cables):
    # Ініціалізуємо купу з довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки не залишиться один кабель
    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислюємо витрати на з'єднання
        cost = first + second
        total_cost += cost
        
        # Додаємо новий з'єднаний кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", minimum_cost_to_connect_cables(cables))
