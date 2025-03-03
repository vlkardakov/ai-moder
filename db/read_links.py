from database import connect_database
from datetime import datetime
import time
import csv
import numpy as np
from checkurlorg import filter_phishing_sites as checkurl

import tldextract

def get_domain(url):
  domain = urlparse(url).netloc # Сначала получаем netloc (доменную часть)
  if not domain:
    return None # Если доменная часть отсутствует, возвращаем None

  extracted = tldextract.extract(domain) # Используем tldextract для разбора домена
  registrable_domain = extracted.domain + '.' + extracted.suffix # Собираем регистрационный домен

  if registrable_domain == '.': # Проверка на случай, если tldextract не смог ничего извлечь (например, для некорректных доменов)
      return None
  if not extracted.domain or not extracted.suffix: # Проверка, что domain и suffix не пустые
      return None

  return registrable_domain

from urllib.parse import urlparse, parse_qs, unquote, urljoin
def decode(url):
    return unquote(unquote(unquote(url)))

def save(table_name, data):
    """
    Сохраняет список словарей в CSV-файл, отсортированный по ключу 'danger' в убывающем порядке.

    Args:
        table_name: Имя файла CSV (без расширения .csv).
        data: Список словарей. Каждый словарь представляет собой строку данных,
              где ключи - имена столбцов, а значения - данные для столбцов.  Должен содержать ключ 'danger'.
    """

    if not data:
        print("Список данных пуст. Ничего не сохранено.")
        return

    if not all(data[0].keys() == d.keys() for d in data):
        print("Ошибка: Словари в списке должны иметь одинаковые ключи, включая ключ 'danger'.")
        return

    try:
        # Преобразуем значения 'danger' в целые числа для корректной сортировки
        for row in data:
            try:
                row['danger'] = int(row['danger'])
            except:
                row['danger'] = 11
        # Сортируем данные по ключу 'danger' в убывающем порядке
        data.sort(key=lambda x: x['danger'], reverse=True)


        with open(f"{table_name}.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Данные успешно сохранены в файл {table_name}.csv")
    except ValueError as e:
        print(f"Ошибка: Значение 'danger' должно быть целым числом: {e}")
    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")

def count_ago(date_str):
    return f"{(s:=(t:=time.time())-time.mktime(time.strptime(date_str, '%Y-%m-%d %H:%M:%S')))//86400:.0f} дней, {(s%86400)//3600 - 3:.0f} часов, {(s%3600)//60:.0f} минут и {s%60:.0f} секунд назад"


def main():
    date = '2025-01-02 00:00:00'
    limit = 1
    connection = connect_database()
    cursor = connection.cursor()
    time1 = time.time()
    cursor.execute(
        "SELECT `url`,`title` ,`ip`, `keyword`, `clicks`, `ads_shown`, `timestamp`"
        "FROM `yourls_url` "
        "WHERE `timestamp` > (%s) AND `clicks` > 1 "
        "ORDER BY `clicks` DESC "
        "LIMIT %s;",
        (date, limit))

    rows = cursor.fetchall()
    links = []
    for el in rows:
            longurl = decode(el[0])
            title = el[1]
            authorip = el[2]
            key = el[3]
            clicks = el[4]
            ads = el[5]
            timestamp = el[6]
            ago = count_ago(str(timestamp))
            domain = get_domain(longurl)

            status, reason = checkurl(cursor, longurl, title, authorip)
            description = f'Ссылка {title}:\n   URL     : {longurl}\n   КЛЮЧ: {key}\n   СТАТУС: {status}\n   ПРИЧИНА: {reason}\n   КЛИКИ   : {clicks}\n   РЕКЛАМА : {ads}\n   ДАТА    : {timestamp}\n   ДАВНОСТЬ: {ago}'


            cursor.execute("SELECT 1 FROM short.black_domain WHERE domain = (%s)", (domain,))
            is_black = cursor.fetchall()
            cursor.execute("SELECT 1 FROM short.white_domain WHERE domain = (%s)", (domain,))
            is_white = cursor.fetchall()
            is_seo = "seo" in status
            if not (is_white or is_black or is_seo) and not 'qw1' in longurl:
                print("+", end='')
                links.append({'url':longurl, 'title':title, 'ip':authorip, 'key':key, 'domain':domain, 'clicks':clicks, 'ads':ads, 'timestamp':timestamp, 'ago':ago, 'status':status, 'reason':reason, 'description':description})
            else:
                print("-", end='')

            # print(f'Ссылка {el[1]}:\n   URL     : {templink}\n   КЛИКИ   : {el[2]}\n   РЕКЛАМА : {el[3]}\n   ДАТА    : {timestamp}\n   ДАВНОСТЬ: {ago}')

    print()
    print(f'В сумме {len(rows)} ссылок, которые не проверены! Прошло всего {time.time() - time1} секунд!')
    # Запись в CSV
    save('links', links)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()