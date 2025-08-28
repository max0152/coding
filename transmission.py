import sqlite3
import time
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('car_statistick.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS CAR_DATA(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    speed REAL,
    transmission INTEGER
)
''')
conn.commit()

def get_transmission(speed):
    if 0 <= speed <= 10:
        return 1
    elif 10 < speed <= 30:
        return 2
    elif 30 < speed <= 50:
        return 3
    elif 50 < speed <= 70:
        return 4
    else:
        return 5

def main():
    speed = random.uniform(0, 20)
    duration_seconds = 60

    for _ in range(duration_seconds):
        delta_speed = random.randint(-10, 10)
        speed += delta_speed

        if speed < 0:
            speed = 0

        transmission = get_transmission(speed)
        print(f"текущая скорость: {speed:.2f} км/ч, передача: {transmission}")

        date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute('''
            INSERT INTO CAR_DATA (date, speed, transmission)
            VALUES (?, ?, ?)
        ''', (date_str, speed, transmission))
        conn.commit()

        time.sleep(0)

    print("\nстатистика за последнюю минуту:")

    one_minute_ago = datetime.now() - timedelta(seconds=60)
    one_minute_str = one_minute_ago.strftime('%Y-%m-%d %H:%M:%S')

    cur.execute('''
        SELECT transmission, COUNT(*) as count
        FROM CAR_DATA
        WHERE datetime(date) >= ?
        GROUP BY transmission
        ORDER BY count DESC
    ''', (one_minute_str,))

    results = cur.fetchall()
    if results:
        print("передачи и их использование за последнюю минуту:")
        for trans, count in results:
            print(f"передача {trans}: использовалась {count} раз(а)")
        
        most_used = results[0]
        print(f"\nсамая часто используемая передача: {most_used[0]} ({most_used[1]} раз)")
    else:
        print("нет данных за последнюю минуту.")

if __name__ == "__main__":
    main()
