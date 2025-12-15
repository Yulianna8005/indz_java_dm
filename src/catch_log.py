"""
Модуль для роботи з локальним журналом виловів у пам'яті.

Цей модуль забезпечує зберігання записів виловів в оперативній пам'яті
без звернення до бази даних.
"""

from typing import List


class CatchLog:
    """
    Локальний журнал виловів у пам'яті.
    
    Накопичує записи про виловлену рибу під час рибальської експедиції
    перед їх збереженням у базу даних.
    """

    def __init__(self) -> None:
        """
        Ініціалізація порожнього журналу виловів.
        """
        self.entries: List[dict] = []

    def add_entry(self, fish_species: str, weight: float) -> None:
        """
        Додавання запису про вилов до журналу.
        
        Параметри:
            fish_species: Вид виловленої риби
            weight: Вага риби у кілограмах
        """
        entry = {
            'species': fish_species,
            'weight': weight
        }
        self.entries.append(entry)
        print(f"[CatchLog] Додано запис: {fish_species} ({weight} кг)")

    def get_entries(self) -> List[dict]:
        """
        Отримання всіх записів з журналу.
        
        Повертає:
            Список записів виловів
        """
        return self.entries.copy()

    def get_total_weight(self) -> float:
        """
        Обчислення загальної ваги всіх виловів.
        
        Повертає:
            Сума ваги всіх записаних риб у кілограмах
        """
        return sum(entry['weight'] for entry in self.entries)

    def get_catch_count(self) -> int:
        """
        Отримання кількості записаних виловів.
        
        Повертає:
            Кількість риб у журналі
        """
        return len(self.entries)

    def clear(self) -> None:
        """
        Очищення журналу від усіх записів.
        """
        self.entries.clear()
        print("[CatchLog] Журнал очищено")

    def display_summary(self) -> None:
        """
        Виведення короткого резюме журналу в консоль.
        """
        print("\n[CatchLog Summary]")
        print(f"  Кількість рибин: {self.get_catch_count()}")
        print(f"  Загальна вага: {self.get_total_weight()} кг")
        if self.entries:
            print("  Деталі виловів:")
            for i, entry in enumerate(self.entries, 1):
                print(f"    {i}. {entry['species']} - {entry['weight']} кг")
        print()
