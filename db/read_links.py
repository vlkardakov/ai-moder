from database import connect_database
from datetime import datetime
import time
import csv
import numpy as np

from urllib.parse import urlparse, parse_qs, unquote, urljoin
def decode(url):
    return unquote(unquote(unquote(url)))

def count_ago(date_str):
    return f"{(s:=(t:=time.time())-time.mktime(time.strptime(date_str, '%Y-%m-%d %H:%M:%S')))//86400:.0f} дней, {(s%86400)//3600 - 3:.0f} часов, {(s%3600)//60:.0f} минут и {s%60:.0f} секунд назад"


def main():
    date = '2025-03-02 15:00:00'
    connection = connect_database()
    cursor = connection.cursor()
    time1 = time.time()
    cursor.execute(
        "SELECT `url`, `title`, `clicks`, `ads_shown`, `timestamp` FROM `yourls_url` WHERE `timestamp` > (%s) AND `clicks` > -1 ORDER BY `clicks` DESC;",
        (date,))

    rows = cursor.fetchall()
    linkss = np.array([])
    for el in rows:
            templink = decode(el[0])
            timestamp = str(el[4])
            ago = count_ago(timestamp)
            print(f'Ссылка {el[1]}:\n   URL     : {templink}\n   КЛИКИ   : {el[2]}\n   РЕКЛАМА : {el[3]}\n   ДАТА    : {timestamp}\n   ДАВНОСТЬ: {ago}')

            linkss = np.append(linkss, templink)

    print(f'В сумме {len(rows)} ссылок! Прошло всего {time.time() - time1} секунд!')
    # Запись в CSV
    with open('links.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(linkss)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()