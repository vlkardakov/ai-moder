from database import connect_database
from fastban import ban_domain

def main():
    connection = connect_database()
    cursor = connection.cursor()
    try:
        while True:
            domain = input('Введите домен для блокировки: ')
            if domain:
                ban_domain(cursor, domain)
                connection.commit()
    except KeyboardInterrupt:
        print('Пока!')

    cursor.close()
    connection.close()
