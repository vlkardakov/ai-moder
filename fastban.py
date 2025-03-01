import mysql.connector
from mysql.connector import Error
import csv

def read_csv(path):
  first = []
  try:
    with open(path, 'r', encoding='utf-8') as csvfile:
      csv_reader = csv.reader(csvfile)
      for row in csv_reader:
        if row:
          first.append(row[0])
    return first
  except FileNotFoundError:
    print(f"Ошибка: Файл не найден: {path}")
    return []
  except Exception as e:
    print(f"Ошибка при чтении файла: {e}")
    return []

def connect_database():
    try:
        connection = mysql.connector.connect(
            host='193.42.111.139',  # IP или домен удалённого сервера
            port=3306,  # Порт MySQL (по умолчанию 3306)
            user='miniurl_top',  # Имя пользователя MySQL
            password='oY1fP2lO5xxZ8uV3hT2w',  # Пароль пользователя
            database='short'  # Имя базы данных
        )

        if connection.is_connected():
            print("Соединение с базой данных установлено :D")
            return connection

    except Error as e:
        print("Ошибка при подключении к базе данных:", e)
        exit()

def ban_domain(cursor, domain):
    try:
        cursor.execute(f"INSERT INTO `short`.`black_domain` (`domain`) VALUES ('{domain}');")
        print(f"Забанен {domain}!")
    except:
        print(f"{domain} не забанен!!")
def main():
    connection = connect_database()
    black_domains = read_csv(r"C:\Users\vlkardakov\Downloads\new.csv")
    if connection.is_connected():
        cursor = connection.cursor()
        for black_domain in black_domains:
            ban_domain(cursor, black_domain)
        print("Закончили, сохраняем...")
        connection.commit()# сохранение
        cursor.close()
        connection.close()
        print("Соединение закрыто")
    else:
        print("ЧТО?")


if __name__ == "__main__":
    #print(read_csv(r"C:\Users\vlkardakov\Downloads\new.csv")) # - Работает.
    main()

"""
if connection.is_connected():
if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor.fetchall():
        print(table)
if connection.is_connected():
    connection.close()
    print("Соединение закрыто")"""