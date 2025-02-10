from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        visited = {}  # Храним {fruit: last_seen_index}
        l = 0  # Левая граница окна
        res = 0

        for r, fruit in enumerate(fruits):
            visited[fruit] = r  # Обновляем последний индекс появления

            if len(visited) > 2:  # Если фруктов больше 2, двигаем левую границу
                min_fruit = min(visited, key=visited.get)  # Фрукт с минимальным индексом
                l = visited[min_fruit] + 1  # Двигаем левую границу вправо
                del visited[min_fruit]  # Удаляем фрукт из памяти

            res = max(res, r - l + 1)  # Обновляем максимум

        return res

solution = Solution()
print(solution.totalFruit([1, 1, 1, 2, 3, 4]))