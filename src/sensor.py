"""
Модуль для роботи з сенсорами моніторингу водойми.

Цей модуль забезпечує імітацію роботи датчиків для вимірювання
температури та якості води.
"""

import random
from typing import Optional


class Sensor:
    """
    Датчик для моніторингу параметрів водойми.
    
    Вимірює температуру та якість води, симулюючи реальні виміри
    з деякою варіативністю.
    """

    def __init__(self, sensor_id: str, location: str) -> None:
        """
        Ініціалізація датчика.
        
        Параметри:
            sensor_id: Унікальний ідентифікатор датчика
            location: Місцезнаходження датчика (назва водойми/ділянки)
        """
        self.sensor_id = sensor_id
        self.location = location
        self.last_temperature: Optional[float] = None
        self.last_quality: Optional[str] = None

    def measure_temperature(self) -> float:
        """
        Вимірювання температури води.
        
        Повертає:
            Температура води у градусах Цельсія (від 5 до 25 градусів)
        """
        # Імітація вимірювання температури з варіативністю
        temperature = round(random.uniform(5, 25), 1)
        self.last_temperature = temperature
        print(f"[Sensor {self.sensor_id}] Температура води в місцезнаходженні '{self.location}': {temperature}°C")
        return temperature

    def measure_water_quality(self) -> str:
        """
        Вимірювання якості води.
        
        Повертає:
            Оцінка якості води: 'Відмінна', 'Хороша' або 'Задовільна'
        """
        # Імітація вимірювання якості води
        quality_options = ['Відмінна', 'Хороша', 'Задовільна']
        quality = random.choice(quality_options)
        self.last_quality = quality
        print(f"[Sensor {self.sensor_id}] Якість води в місцезнаходженні '{self.location}': {quality}")
        return quality

    def get_sensor_data(self) -> dict:
        """
        Отримання останніх вимірів датчика.
        
        Повертає:
            Словник з ідентифікатором, місцезнаходженням, температурою та якістю
        """
        return {
            'sensor_id': self.sensor_id,
            'location': self.location,
            'temperature': self.last_temperature,
            'quality': self.last_quality
        }

    def __str__(self) -> str:
        """
        Рядкова репрезентація датчика.
        
        Повертає:
            Рядок з інформацією про датчик
        """
        return f"Sensor(id={self.sensor_id}, location={self.location})"
