"""
Модуль для роботи з сервісом прогнозу погоди.

Цей модуль забезпечує імітацію отримання прогнозу погоди для планування
рибальської експедиції.
"""

import random
from typing import Optional


class WeatherService:
    """
    Сервіс для отримання прогнозу погоди.
    
    Симулює роботу служби погоди та надає прогноз для планування
    рибальської діяльності.
    """

    @staticmethod
    def get_weather_forecast(location: str) -> dict:
        """
        Отримання прогнозу погоди для локації.
        
        Параметри:
            location: Назва локації для прогнозу
            
        Повертає:
            Словник з прогнозом погоди (температура, вітер, опади)
        """
        print(f"\n[WeatherService] Отримую прогноз погоди для місцезнаходження '{location}'")
        
        temperature = random.randint(10, 25)
        wind_speed = random.randint(0, 20)
        precipitation = random.choice(['Немає', 'Низька', 'Висока'])
        conditions = random.choice(['Сонячно', 'Хмарно', 'Дощово'])
        
        forecast = {
            'location': location,
            'temperature': temperature,
            'wind_speed': wind_speed,
            'precipitation': precipitation,
            'conditions': conditions
        }
        
        print(f"[Weather Forecast - {location}]")
        print(f"  Температура: {temperature}°C")
        print(f"  Вітер: {wind_speed} км/год")
        print(f"  Опади: {precipitation}")
        print(f"  Умови: {conditions}")
        
        return forecast

    @staticmethod
    def is_suitable_for_fishing(forecast: dict) -> bool:
        """
        Перевірка придатності погоди для риболовлі.
        
        Параметри:
            forecast: Словник з прогнозом погоди
            
        Повертає:
            True, якщо умови придатні для риболовлі, інакше False
        """
        temperature = forecast.get('temperature', 0)
        wind_speed = forecast.get('wind_speed', 0)
        
        # Умови придатні, якщо температура від 10 до 25 і вітер до 15 км/год
        is_suitable = 10 <= temperature <= 25 and wind_speed <= 15
        
        status = "✓ Придатні" if is_suitable else "✗ Непридатні"
        print(f"[Weather Assessment] Умови для риболовлі: {status}\n")
        
        return is_suitable
