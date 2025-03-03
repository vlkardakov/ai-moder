import pandas as pd
from urllib.parse import unquote
import csv

def remove_rows_containing_words_and_duplicates_pandas(input_file, output_file, bad_words, processed_fingerprints_file):
    processed_fingerprints = set()
    try:
        try:
            with open(processed_fingerprints_file, 'r', encoding='utf-8') as f:
                processed_fingerprints = set(line.strip() for line in f)
        except FileNotFoundError:
            pass # Файл с отпечатками еще не создан, начинаем с нуля

        df = pd.read_csv(input_file, encoding='utf-8')

        # Удаление строк с указанными словами
        df = df[~df.apply(lambda row: any(word in str(val).lower() for val in row for word in bad_words), axis=1)]

        # Декодирование URL-адресов (предполагается, что URL находятся в столбце с именем 'url')
        if 'url' in df.columns:
          df['url'] = df['url'].apply(lambda x: unquote(x) if isinstance(x, str) else x)


        new_rows = []
        new_fingerprints = set()

        for index, row in df.iterrows():
            row_tuple = tuple(row.astype(str)) # Преобразуем строку в кортеж для хеширования
            fingerprint = hash(row_tuple) # Генерируем отпечаток строки
            if str(fingerprint) not in processed_fingerprints: # Проверяем, не обрабатывалась ли строка ранее
                new_rows.append(row)
                new_fingerprints.add(str(fingerprint))

        if not new_rows:
            print("Нет новых данных для добавления, все дубликаты или уже обработаны.")
            return

        df_new = pd.DataFrame(new_rows)

        if output_file and output_file != input_file: # Если указан выходной файл и он отличается от входного, сохраняем в новый файл
            try:
                df_output = pd.read_csv(output_file, encoding='utf-8') # Пытаемся загрузить существующий выходной файл
                df_final = pd.concat([df_output, df_new], ignore_index=True) # Объединяем с новыми данными
            except FileNotFoundError: # Если выходной файл не существует, просто используем новые данные
                df_final = df_new

            df_final.drop_duplicates(subset=None, inplace=True) # Удаляем дубликаты уже после объединения
            df_final.to_csv(output_file, index=False, encoding='utf-8')
            print(f"Результат сохранен в {output_file}")
        else: # Если выходной файл не указан или совпадает с входным, перезаписываем входной файл
            df_new.drop_duplicates(subset=None, inplace=True) # Удаляем дубликаты
            df_new.to_csv(input_file, index=False, encoding='utf-8') # Перезаписываем входной файл
            print(f"Результат сохранен в {input_file} (входной файл перезаписан)")


        updated_fingerprints = processed_fingerprints.union(new_fingerprints)
        with open(processed_fingerprints_file, 'w', encoding='utf-8') as f:
            for fp in updated_fingerprints:
                f.write(f"{fp}\n")


    except FileNotFoundError:
        print(f"Файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def pithon(code):
    global result
    try:
        local_vars = {}
        exec(code, {}, local_vars)  # Используем локальный словарь для хранения переменных
        return local_vars.get('result')  # Возвращаем значение переменной result
    except Exception as e:
        return e


def load_checked():
    try:
        with open("checked_domains.txt", "r") as f:
            content = f.read()
            if content.strip(): # Проверяем, что файл не пустой и не состоит только из пробелов
                return pithon(f"result = {content}") or [] # Возвращаем пустой список, если pithon вернет None
            else:
                return [] # Возвращаем пустой список, если файл пустой
    except FileNotFoundError:
        return [] # Возвращаем пустой список, если файл не найден
    except Exception as e:
        print(f"Ошибка при загрузке checked_domains.txt: {e}")
        return [] # Возвращаем пустой список в случае ошибки

def clean():
    # Пример использования:
    input_file = "1.csv"
    output_file = "1_fixed.csv" # Можно указать тот же input_file для перезаписи входного файла
    processed_fingerprints_file = "processed_fingerprints.txt" # Файл для хранения отпечатков обработанных строк
    remove_rows_containing_words_and_duplicates_pandas(input_file, output_file, processed_fingerprints_file)