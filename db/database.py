import mysql.connector
from mysql.connector import Error
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
