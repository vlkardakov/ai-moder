import pandas as pd
import csv

def pandas_column_to_array(filename):
    try:
        df = pd.read_csv(filename, encoding='utf-8')
        if df.empty:  # Проверка на пустой DataFrame
          print(f"Файл пуст.")
          return []
        first_column_name = df.columns[0]  # Получение имени первого столбца
        column_array = df[first_column_name].tolist()
        return column_array
    except FileNotFoundError:
        print(f"Файл не найден.")
        return None
    except Exception as e:
        print(f"{e}")
        return None

def read(table_name):
    """
    Читает данные из CSV-файла и возвращает список словарей.

    Args:
        table_name: Имя файла CSV (без расширения .csv).

    Returns:
        Список словарей, где каждый словарь представляет собой строку из CSV-файла.
        Возвращает пустой список, если файл не найден или произошла ошибка чтения.
    """
    try:
        with open(f"{table_name}.csv", "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader) # Преобразуем итератор в список словарей
        print(f"Данные успешно прочитаны из файла {table_name}.csv")
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл {table_name}.csv не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении из CSV: {e}")
        return []

# def read():
#     filename = "1_fixed.csv"
#     column_array = pandas_column_to_array(filename)
#
#     if column_array is not None:
#         # print(column_array)
#         return column_array
#     else:
#         return []