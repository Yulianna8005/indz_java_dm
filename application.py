#!/usr/bin/env python3
"""
Головна програма для демонстрації системи управління рибальством.

Цей модуль демонструє взаємодію всіх компонентів системи:
- Рибалка планує та виконує риболовлю
- Сенсори моніторять умови водойми
- Еколог аналізує стан навколишнього середовища
- Журнал виловів зберігає інформацію в SQLite БД
"""

import sys
import os

# Додавання папки src до шляху пошуку модулів
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from catch_log_service import CatchLogService
from fisherman import Fisherman
from sensor import Sensor
from ecologist import Ecologist
from fishing_trip import FishingTrip
from weather_service import WeatherService


def print_header(title: str) -> None:
    """
    Виведення форматованого заголовка.
    
    Параметри:
        title: Текст заголовка
    """
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def main() -> None:
    """
    Головна функція програми.
    
    Демонструє повний цикл рибальської експедиції:
    - Планування виходу на воду
    - Моніторинг умов
    - Риболовля та реєстрація виловів
    - Екологічна оцінка
    """
    
    print_header("СИСТЕМА УПРАВЛІННЯ РИБАЛЬСТВОМ")
    print("Демонстрація об'єктно-орієнтованої системи рибальства на Python")
    print()

    # Ініціалізація компонентів системи
    print("[Initialization] Ініціалізація компонентів системи")
    
    # Сервіс журналу виловів з SQLite БД
    catch_log_service = CatchLogService("fishing.db")
    
    # Рибалка
    fisherman = Fisherman("Петро", catch_log_service)
    
    # Сенсори для моніторингу
    sensor_main = Sensor("SENSOR_01", "Озеро Победы")
    sensor_secondary = Sensor("SENSOR_02", "Річка Грабовець")
    
    # Еколог
    ecologist = Ecologist("Марія Коваленко")
    
    # Прогноз погоди
    location = "Озеро Победы"
    weather_forecast = WeatherService.get_weather_forecast(location)
    
    print()
    print("[System Status] Всі компоненти успішно ініціалізовані")
    print()

    # Фаза 1: Планування виходу
    print_header("ФАЗА 1: ПЛАНУВАННЯ ВИХОДУ НА ВОДУ")
    
    fisherman.display_info()
    
    # Перевірка придатності погоди
    is_suitable = WeatherService.is_suitable_for_fishing(weather_forecast)
    
    if not is_suitable:
        print("[Planning] Погода непридатна, експедиція відкладена")
        return
    
    # Перевірка карт та точок
    fisherman.check_depth_map()
    fisherman.check_fishing_spots()
    
    # Екологічна перевірка
    ecologist.analyze_environment(location)
    
    # Створення та запуск експедиції
    fishing_spots = ["Біля берега", "В центрі", "Біля острова"]
    fishing_trip = FishingTrip(location, fisherman.name, "Карта 2024", fishing_spots)
    fishing_trip.start()
    
    print(fishing_trip.get_fishing_plan())

    # Фаза 2: Риболовля
    print_header("ФАЗА 2: ПРОЦЕС РИБОЛОВЛІ")
    
    fisherman.start_fishing(location)
    
    # Моніторинг умов сенсорами
    print("[Environmental Monitoring] Одержання даних від сенсорів")
    ecologist.get_water_condition_report(sensor_main)
    
    # Симуляція риболовлі
    print("[Fishing Simulation] Рибалка виловлює рибу")
    catches = [
        ("Окунь", 0.8),
        ("Щука", 2.5),
        ("Карась", 0.6),
        ("Сом", 3.2),
    ]
    
    for fish_species, weight in catches:
        print(f"\n[FishingAction] Вилучення {fish_species} вагою {weight} кг")
        fisherman.log_catch(fish_species, weight)
    
    print()

    # Фаза 3: Завершення експедиції
    print_header("ФАЗА 3: ЗАВЕРШЕННЯ ЕКСПЕДИЦІЇ")
    
    fisherman.end_fishing()
    fishing_trip.end()
    
    # Отримання зведення з БД
    summary = fisherman.get_catch_summary()
    print(f"[Database Summary] Зведення з бази даних:")
    print(f"  Загальна кількість рибин: {summary['count']}")
    print(f"  Загальна вага: {summary['total_weight']} кг")
    print()

    # Фаза 4: Екологічна оцінка
    print_header("ФАЗА 4: ЕКОЛОГІЧНА ОЦІНКА")
    
    ecologist.get_water_condition_report(sensor_secondary)
    
    # Рекомендації на основі даних
    print("[Recommendations]")
    print("  ✓ Умови водойми придатні для подальшої риболовлі")
    print("  ✓ Якість води на задовільному рівні")
    print("  ✓ Рекомендується збільшити частоту екологічного моніторингу")
    print()

    # Завершення
    print_header("ЕКСПЕДИЦІЯ ЗАВЕРШЕНА")
    print(f"Дякуємо за використання системи управління рибальством!")
    print()


if __name__ == "__main__":
    try:
        main()
        print("[Exit] Програма завершена успішно")
    except KeyboardInterrupt:
        print("\n[Exit] Програма переривається користувачем")
    except Exception as e:
        print(f"\n[Error] Помилка при виконанні програми: {e}")
        import traceback
        traceback.print_exc()
