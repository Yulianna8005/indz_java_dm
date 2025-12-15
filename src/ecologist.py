"""
Модуль для роботи з екологічним моніторингом.

Цей модуль забезпечує аналіз та звітування про умови водойми
на основі даних сенсорів.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sensor import Sensor


class Ecologist:
    """
    Еколог для аналізу стану водойми.
    
    Отримує дані від сенсорів і надає детальний звіт про умови
    навколишнього середовища та якість води.
    """

    def __init__(self, name: str) -> None:
        """
        Ініціалізація еколога.
        
        Параметри:
            name: Ім'я еколога
        """
        self.name = name

    def get_water_condition_report(self, sensor: 'Sensor') -> None:
        """
        Отримання детального звіту про умови води за даними датчика.
        
        Параметри:
            sensor: Датчик для отримання вимірів
        """
        print(f"\n[Ecologist {self.name}] Отримую звіт про умови води")
        
        temperature = sensor.measure_temperature()
        quality = sensor.measure_water_quality()
        
        print(f"\n[Water Condition Report - {self.name}]")
        print(f"  Місцезнаходження: {sensor.location}")
        print(f"  Температура води: {temperature}°C")
        print(f"  Якість води: {quality}")
        
        # Аналіз умов на основі виміру
        self._analyze_conditions(temperature, quality)
        print()

    def analyze_environment(self, location: str) -> None:
        """
        Загальний аналіз стану навколишнього середовища в локації.
        
        Параметри:
            location: Назва локації для аналізу
        """
        print(f"\n[Ecologist {self.name}] Аналізую стан навколишнього середовища в місцезнаходженні '{location}'")
        print(f"[Environmental Analysis]")
        print(f"  Локація: {location}")
        print(f"  Тип екосистеми: Прісноводна водойма")
        print(f"  Статус: Під моніторингом")
        print(f"  Рекомендація: Дотримуватися нормативів вилову")
        print()

    def _analyze_conditions(self, temperature: float, quality: str) -> None:
        """
        Внутрішній аналіз умов води на основі виміру.
        
        Параметри:
            temperature: Виміряна температура
            quality: Виміряна якість води
        """
        print(f"  Аналіз:")
        
        if temperature < 10:
            print(f"    - Температура низька, риба буде менш активною")
        elif temperature > 20:
            print(f"    - Температура висока, умови сприятливі для більшості видів")
        else:
            print(f"    - Температура оптимальна для риболовлі")
        
        if quality == 'Відмінна':
            print(f"    - Якість води відмінна, умови сприятливі для екосистеми")
        elif quality == 'Хороша':
            print(f"    - Якість води хороша, стан екосистеми задовільний")
        else:
            print(f"    - Якість води задовільна, необхідний моніторинг")
