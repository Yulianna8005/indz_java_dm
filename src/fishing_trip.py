"""
Модуль для управління рибальською експедицією.

Цей модуль описує рибальську експедицію з інформацією про місцезнаходження,
учасників та діяльність.
"""

from typing import List, Optional
from datetime import datetime


class FishingTrip:
    """
    Рибальська експедиція з планом та інформацією про виловів.
    
    Управління однією рибальською експедицією включає місцезнаходження,
    учасників, час початку та записи виловів.
    """

    def __init__(self, location: str, fisherman_name: str, 
                 depth_map: str, fishing_spots: List[str]) -> None:
        """
        Ініціалізація рибальської експедиції.
        
        Параметри:
            location: Назва водойми/місцезнаходження
            fisherman_name: Ім'я рибалки-організатора
            depth_map: Інформація про карту глибин
            fishing_spots: Список точок кльову
        """
        self.location = location
        self.fisherman_name = fisherman_name
        self.depth_map = depth_map
        self.fishing_spots = fishing_spots
        self.start_time = datetime.now()
        self.end_time: Optional[datetime] = None
        self.is_active = False

    def start(self) -> None:
        """
        Розпочати рибальську експедицію.
        """
        self.is_active = True
        self.start_time = datetime.now()
        print(f"\n[FishingTrip] Експедиція розпочата в місцезнаходженні '{self.location}'")
        print(f"  Рибалка: {self.fisherman_name}")
        print(f"  Карта глибин: {self.depth_map}")
        print(f"  Точки кльову: {', '.join(self.fishing_spots)}")
        print()

    def end(self) -> None:
        """
        Завершити рибальську експедицію.
        """
        self.is_active = False
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).total_seconds() / 60
        print(f"\n[FishingTrip] Експедиція завершена")
        print(f"  Місцезнаходження: {self.location}")
        print(f"  Тривалість: {duration:.0f} хвилин")
        print()

    def get_fishing_plan(self) -> str:
        """
        Отримання плану рибальської експедиції.
        
        Повертає:
            Текстовий опис плану експедиції
        """
        plan = f"""
[Fishing Plan]
Місцезнаходження: {self.location}
Рибалка: {self.fisherman_name}
Карта глибин: {self.depth_map}
Точки кльову: {', '.join(self.fishing_spots)}
Статус: {'Активна' if self.is_active else 'Неактивна'}
"""
        return plan

    def __str__(self) -> str:
        """
        Рядкова репрезентація експедиції.
        
        Повертає:
            Рядок з основною інформацією про експедицію
        """
        return f"FishingTrip(location={self.location}, fisherman={self.fisherman_name}, active={self.is_active})"
