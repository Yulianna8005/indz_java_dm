"""
Модуль для управління рибалкою та його діяльністю.

Цей модуль описує рибалку як основний учасник системи з можливістю
планування, риболовлі та реєстрації виловів.
"""

from typing import Optional
from catch_log import CatchLog
from catch_log_service import CatchLogService


class Fisherman:
    """
    Рибалка - основний учасник рибальської системи.
    
    Здійснює риболовлю, перевіряє карти глибин та точки кльову,
    реєструє виловів у журналі та базі даних.
    """

    def __init__(self, name: str, catch_log_service: CatchLogService) -> None:
        """
        Ініціалізація рибалки.
        
        Параметри:
            name: Ім'я рибалки
            catch_log_service: Сервіс для збереження журналу виловів
        """
        self.name = name
        self.location: Optional[str] = None
        self.catch_log = CatchLog()
        self._catch_log_service = catch_log_service
        self.is_fishing = False

    def set_catch_log_service(self, service: CatchLogService) -> None:
        """
        Встановлення (setter injection) сервісу журналу виловів.
        
        Параметри:
            service: Новий сервіс журналу виловів
        """
        self._catch_log_service = service
        print(f"[Fisherman {self.name}] Встановлено новий сервіс журналу виловів")

    def check_depth_map(self) -> None:
        """
        Перевірка карти глибин водойми.
        """
        print(f"\n[Fisherman {self.name}] Перевіряю карту глибин")
        print(f"  Глибина в місцезнаходженні '{self.location}': від 1 до 5 метрів")
        print(f"  Рекомендація: Оптимально для риболовлі на глибині 2-3 метри")
        print()

    def check_fishing_spots(self) -> None:
        """
        Перевірка точок кльову на водоймі.
        """
        print(f"\n[Fisherman {self.name}] Перевіряю точки кльову")
        spots = ['Біля берега', 'В центрі водойми', 'Біля рослинності', 'На російськ', 'Біля острова']
        for spot in spots:
            print(f"  ✓ {spot}")
        print()

    def start_fishing(self, location: str) -> None:
        """
        Розпочати риболовлю в конкретній локації.
        
        Параметри:
            location: Назва водойми/місцезнаходження
        """
        self.location = location
        self.is_fishing = True
        self.catch_log.clear()  # Очистити журнал перед новою експедицією
        print(f"\n[Fisherman {self.name}] Розпочинаю риболовлю в місцезнаходженні '{location}'")
        print(f"  Статус: Активно риблю")
        print()

    def log_catch(self, fish_species: str, weight: float) -> None:
        """
        Реєстрація виловленої риби у журналі та базі даних.
        
        Параметри:
            fish_species: Вид риби
            weight: Вага риби у кілограмах
        """
        if not self.is_fishing:
            print(f"[Fisherman {self.name}] Ошибка: Вы не на рыбалке!")
            return
        
        # Додати до локального журналу
        self.catch_log.add_entry(fish_species, weight)
        
        # Зберегти в базу даних
        if self._catch_log_service:
            self._catch_log_service.save_catch(self.name, fish_species, weight)

    def end_fishing(self) -> None:
        """
        Завершити риболовлю та вивести звіт про виловів.
        """
        if not self.is_fishing:
            print(f"[Fisherman {self.name}] Вже не на рибалці")
            return
        
        self.is_fishing = False
        print(f"\n[Fisherman {self.name}] Завершую риболовлю в місцезнаходженні '{self.location}'")
        self.catch_log.display_summary()

    def get_catch_summary(self) -> dict:
        """
        Отримання зведеної інформації про виловів.
        
        Повертає:
            Словник з кількістю та загальною вагою виловів
        """
        return self._catch_log_service.get_catch_summary(self.name)

    def display_info(self) -> None:
        """
        Виведення інформації про рибалку в консоль.
        """
        print(f"\n[Fisherman Info]")
        print(f"  Ім'я: {self.name}")
        print(f"  Поточне місцезнаходження: {self.location or 'На берегу'}")
        print(f"  Статус: {'Активна риболовля' if self.is_fishing else 'Неактивна'}")
        print()

    def __str__(self) -> str:
        """
        Рядкова репрезентація рибалки.
        
        Повертає:
            Рядок з інформацією про рибалку
        """
        return f"Fisherman(name={self.name}, location={self.location}, fishing={self.is_fishing})"
