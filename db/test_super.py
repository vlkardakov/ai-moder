from database_super import connect_database

if __name__ == '__main__':
    connection = connect_database()
    cursor = connection.cursor()
    try:
        while True:
            query = ''
            print(r'Введите запрос:')
            text = input()
            while text != '':
                query += f'\n{text}'
                text = input()


            # print(f'Вы ввели запрос: \n{query}')
            try:
                cursor.execute(query)
            except Exception as e:
                print(f'Ошибка при выполнении запроса: {e}')
            print(cursor.fetchall())
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(row)
    except KeyboardInterrupt:
        connection.commit()# сохранение
        cursor.close()
        connection.close()
        print("BYE!")