"""
Модуль для роботи з базою даних журналу виловів.

Цей модуль забезпечує зберігання та управління записами виловів риби
у SQLite базі даних.
"""

import sqlite3
from typing import List
from datetime import datetime


class CatchLogService:
    """
    Сервіс для управління журналом виловів в SQLite базі даних.
    
    Забезпечує зберігання записів про виловлену рибу з інформацією
    про рибалку, тип риби та вагу.
    """

    def __init__(self, db_path: str = "fishing.db") -> None:
        """
        Ініціалізація сервісу журналу виловів.
        
        Параметри:
            db_path: Шлях до файлу SQLite бази даних (за замовчуванням: fishing.db)
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        """
        Ініціалізація бази даних та створення таблиці виловів, якщо її немає.
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS catches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fisherman_name TEXT NOT NULL,
                    fish_species TEXT NOT NULL,
                    weight REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            connection.commit()
            connection.close()
            print("[Database] Таблицю 'catches' успішно ініціалізовано")
        except sqlite3.Error as e:
            print(f"[Database Error] Помилка при ініціалізації бази даних: {e}")

    def save_catch(self, fisherman_name: str, fish_species: str, weight: float) -> None:
        """
        Збереження запису про вилов риби в базу даних.
        
        Параметри:
            fisherman_name: Ім'я рибалки
            fish_species: Вид риби
            weight: Вага риби у кілограмах
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            
            cursor.execute("""
                INSERT INTO catches (fisherman_name, fish_species, weight)
                VALUES (?, ?, ?)
            """, (fisherman_name, fish_species, weight))
            
            connection.commit()
            connection.close()
            print(f"[CatchLogService] Вилов '{fish_species}' ({weight} кг) для '{fisherman_name}' збережено в БД")
        except sqlite3.Error as e:
            print(f"[Database Error] Помилка при збереженні виловії: {e}")

    def get_all_catches(self, fisherman_name: str = None) -> List[dict]:
        """
        Отримання всіх записів виловів з бази даних.
        
        Параметри:
            fisherman_name: Фільтр за іменем рибалки (опціонально)
            
        Повертає:
            Список словників з інформацією про виловів
        """
        try:
            connection = sqlite3.connect(self.db_path)
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            
            if fisherman_name:
                cursor.execute("""
                    SELECT * FROM catches WHERE fisherman_name = ? ORDER BY timestamp DESC
                """, (fisherman_name,))
            else:
                cursor.execute("SELECT * FROM catches ORDER BY timestamp DESC")
            
            rows = cursor.fetchall()
            connection.close()
            
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            print(f"[Database Error] Помилка при читанні даних: {e}")
            return []

    def get_catch_summary(self, fisherman_name: str) -> dict:
        """
        Отримання зведеної інформації про виловів конкретного рибалки.
        
        Параметри:
            fisherman_name: Ім'я рибалки
            
        Повертає:
            Словник з кількістю та загальною вагою виловів
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            
            cursor.execute("""
                SELECT COUNT(*) as count, SUM(weight) as total_weight
                FROM catches WHERE fisherman_name = ?
            """, (fisherman_name,))
            
            result = cursor.fetchone()
            connection.close()
            
            return {
                'count': result[0] or 0,
                'total_weight': result[1] or 0.0
            }
        except sqlite3.Error as e:
            print(f"[Database Error] Помилка при отриманні зведення: {e}")
            return {'count': 0, 'total_weight': 0.0}
