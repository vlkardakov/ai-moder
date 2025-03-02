from database import connect_database
import time
import csv
import numpy as np

from urllib.parse import urlparse, parse_qs, unquote, urljoin
def decode(url):
    return unquote(unquote(unquote(url)))

def main():
    date = '2025-03-02 10:18:00'
    connection = connect_database()
    cursor = connection.cursor()
    time1 = time.time()
    cursor.execute("SELECT `url`, `title`, `clicks`, `ads_shown` FROM `yourls_url` WHERE `timestamp` > (%s) AND `clicks` > 2;", (date,))
    rows = cursor.fetchall()
    linkss = np.array([])
    for el in rows:

            templink = decode(el[0])
            print(f'Ссылка {el[1]}:\n   URL:{templink}\n   КЛИКИ:{el[2]}\n   РЕКЛАМА:{el[3]}')

            linkss = np.append(linkss, templink)

    print(f'В сумме {len(rows)} ссылок! Прошло всего {time1 - time.time()} секунд!')
    # Запись в CSV
    with open('links.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(linkss)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()