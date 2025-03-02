import csv
from database import connect_database
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


def ban_domain(cursor, domain):
    try:
        cursor.execute("INSERT INTO `short`.`black_domain` (`domain`) VALUES (%s);", (domain,))
        print(f"+ {domain}!")
    except:
        print(f"- {domain} ")
def main():
    connection = connect_database()
    black_domains = read_csv(r"C:\Users\vlkardakov\Downloads\new.csv")
    if connection.is_connected():
        print("///")
        cursor = connection.cursor()
        for black_domain in black_domains:
            ban_domain(cursor, black_domain)
        print("///")

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