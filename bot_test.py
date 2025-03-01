import random

import telebot
import pandas as pd
import time
import os
import io

TOKEN = '7923293677:AAH9l0wC1StMncKbrY1yuVpgP65JR80LWVw'  # Замените на ваш токен
bot = telebot.TeleBot(TOKEN)

import subprocess
from PIL import ImageGrab, Image
import mss
import cv2 as cv
import numpy as np
import datetime
from module import describe
import time
from cleancsv import clean
from read import read
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from linkprocessing import process_links
from save import save
from decode import process_url, final_link

print("imported")


async def get_final_url_base(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, allow_redirects=True) as response:
                response.raise_for_status()  # Проверка на ошибки
                result = response.url
                if isinstance(result, bytes):
                    result = result.decode('utf-8', errors='replace')
                return result
    except aiohttp.ClientError as e:
        print(f"Ошибка при запросе: {e}")
        return None

async def get_final_url(url):  # Замените на ваш URL
    final_url = await get_final_url_base(url)
    if final_url:
        return final_url

async def get_page_title(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else None
            return title.strip() if title else None
    except aiohttp.ClientError as e:
        # print(f"Ошибка при запросе ({url}): {e}")
        return None
    except AttributeError:
        # print(f"Заголовок не найден на странице ({url}).")
        return None

async def get_page_titles(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [get_page_title(session, url) for url in urls]
        titles = await asyncio.gather(*tasks)
        return titles


def pithon(code):
    global result
    try:
        local_vars = {}
        exec(code, {}, local_vars)  # Используем локальный словарь для хранения переменных
        return local_vars.get('result')  # Возвращаем значение переменной result
    except Exception as e:
        return e


def save_checked(checked):
    with open("checked_domains.txt", "w") as f:
        f.write(str(checked))


def load_checked():
    with open("checked_domains.txt", "r") as f:
        return pithon(f"result = {f.read()}")


def save_verified(checked):
    with open("verified_domains.txt", "w") as f:
        f.write(str(checked))


def load_verified():
    with open("verified_domains.txt", "r") as f:
        return pithon(f"result = {f.read()}")


def open_screenshot(filename):
    img = Image.open(filename)
    return img


def translate(text):
    return GoogleTranslator(source='auto', target='ru').translate(text)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Отправьте таблицу CSV")


from datetime import datetime


def get_tag():
    now = datetime.now()
    formatted = now.strftime("%y-%m-%d-%H")
    return formatted


def send(text):
    subprocess.run(["press.exe", text])


stop_processing = False


def split_array(arr, chunk_size=7):
    return np.array_split(arr, np.ceil(len(arr) / chunk_size))


@bot.message_handler(commands=['stop'])
def stop_processing_command(message):
    global stop_processing
    stop_processing = True
    bot.reply_to(message, "Обработка остановлена. Подождите завершения...")


@bot.message_handler(commands=['exit'])
def stop_processing_command(message):
    bot.reply_to(message, "ОТКЛЮЧЕНИЕ.")
    os.system("taskkill /IM python.exe /F")


@bot.message_handler(commands=['restart'])
def stop_processing_command(message):
    bot.reply_to(message, " Ухожу на перезагрузку..")
    os.system("start UPDATE.exe")
    exit()


@bot.message_handler(content_types=['document'])
def handle_document(message):
    global stop_processing
    stop_processing = False
    try:
        os.remove("ОТЧЁТ.csv")
    except:
        pass
    if message.document.mime_type == 'text/csv':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('1.csv', 'wb') as new_file:
            new_file.write(downloaded_file)

        # bot.reply_to2222(message, f"Файл успешно сохранён. Обнаружено {num_rows} ссылок. (займет примерно {time.strftime('%H:%M:%S', time.gmtime(num_rows*7))}) Начать обработку? (Да/Нет)")
        bot.reply_to(message, f"Файл успешно сохранён. Начать обработку?")

        # Начинаем ожидание ответа пользователя
        @bot.message_handler(func=lambda message: message.text.lower() in ['да', 'нет'])
        def handle_processing_decision(message):
            global stop_processing
            if message.text.lower() == 'да':
                # bot.reply_to(message, f"Обработка начата... Я пришлю таблицу меньше чем через {time.strftime('%H:%M:%S', time.gmtime(num_rows*7))}")
                bot.reply_to(message, f"Обработка начата... ")

                time1 = time.time()
                # bot.reply_to(message, f"Время задано")

                # Очищаем от мусора
                checked_domains = load_checked()
                # bot.reply_to(message, f"Домены загружены")
                err_tag = get_tag()
                # bot.reply_to(message, f"Тэг получен")
                clean()
                # bot.reply_to(message, f"таблицы очищена")
                scams = []
                readed = read()
                # random.shuffle(readed)
                urls_not_sorted = readed

                total_links_not_sorted = np.array([], dtype=str)

                urls = process_links(readed)

                bot.reply_to(message, f"Таблица прочитана")
                using_len = len(urls)
                if using_len > 0:
                    bot.reply_to(message, f"Найдено {using_len} нормальных ссылок!")
                    for i in range(using_len):
                        if stop_processing:
                            break
                        elif random.randint(0, 10) < 2:
                            save(f"ОТЧЁТ", scams)
                            save_checked(checked_domains)
                        try:
                            link = urls[i]
                            if not link:
                                continue
                            time_start_domains = time.time()
                            url = link["url"]
                            domain = link['domain']
                            title = link["title"]
                            screenshot_path = link['screenshot']


                            print(f"Cсылка: {url}, Title: {title}, Скриншот: {screenshot_path}, Домен: {domain}")



                            time.sleep(0.1)

                            try:
                                print("translating")
                                title = translate(title)
                            except:
                                pass
                            time.sleep(4)
                            time_start_generation = time.time()
                            prompt = \
                                f"""Ты должен описать, что ты видишь, и считаешь ли, что сайт - мошеннический. Не более 2000 символов!!!
Признаки мошеннических сайтов: говорят, что покупатель оплатил товар и просят получить деньги, всякие казино, другие розыгрыши, закос под службы доставки или интернет-магазины. 
Уделя внимание Самому URL адресу, например amazon.s4674.world может выглядеть как сайт amazon, но быть мошенническим.
Так же определяй, что сайт содержит 18+ контент, или например являются сервисами сокращения ссылок (мошенничество и так далее.

типы сайтов: хороший, новости, форум, сократители ссылок, легитимный, (означает, что принадлежит известной компании), мошенничество, казино, 18+

В ответе выдай (разделительные символы между ЧАСТЯМИ - "|": рассуждения коротко|тип|оценка опасности сайта от 0 до 10 1, целым числом
Пример ответа: "Сайт Google | легитимный | 0"
Другой пример: "Редирект на казино | казино | 8"
url и title сайта для проверки, структура url - title: {url} - {title}"""
                            print("Пытаемся объяснить страницу")
                            img = open_screenshot(screenshot_path)
                            result = describe(prompt, img).split("|")

                            print(f"{result[-3]}")
                            print(f"Тип        : {result[-2]}")
                            print(f"Опасность  : {result[-1]}")
                            print(f"Времени на генерацию: {time.time() - time_start_generation}")
                            # ПИПЕЦ
                            if "хороший" in result[1]:
                                pass
                            elif "легитимный" in result[1]:
                                pass
                            elif result[1] in ("хороший", 'легитимный', 'новости', 'сократители ссылок', 'форум'):
                                pass
                            else:
                                print("Записываем в скам")
                                scams.append(
                                    {"type": result[1], "danger": result[2], "url": url,
                                     "thoughts": result[0],
                                     "domain": domain, "title": title,
                                     "time": time.time() - time_start_domains})
                            try:
                                with open(screenshot_path, "rb") as img_file:
                                    bot.send_photo(message.chat.id, img_file,
                                                   caption=f"""URL: {url[:100]} - {title[:100]}\n{result[-3]}\n\nТип        : {result[-2]}\nОпасность  : {result[-1]}\nРасчётное время : {time.strftime('%H:%M:%S', time.gmtime((((using_len - 1) - i) * 10)))}""".encode(
                                                       'utf-8'))


                            except:
                                pass
                            print(f"Времени на всё: {time.time() - time_start_domains}")
                        except Exception as e:
                            print(f"Пока пытались объяснить, проищоошла ошибка {e}")

                    print("РАБОТА ОКОНЧЕНА, СОХРАНЕНИЕ")
                    save(f"ОТЧЁТ", scams)

                    save_checked(checked_domains)
                    print("ОТКЛЮЧЕНИЕ")
                    print(f"{checked_domains=}")

                    time.sleep(4)
                    if os.path.exists('ОТЧЁТ.csv'):
                        with open('ОТЧЁТ.csv', 'rb') as report:
                            bot.send_document(message.chat.id, report,
                                              caption=f"Запрос занял {time.time() - time1} секунд")
                            time.sleep(5)
                        try:
                            os.remove("ОТЧЁТ.csv")
                        except:
                            pass
                        bot.reply_to(message,
                                     f"Готов!")
                        # stop_processing = False
                    else:
                        bot.reply_to(message,
                                     f"Мошеннических сайтов не обнаружено. Запрос занял {time.time() - time1} секунд")

                bot.reply_to(message, "Все ссылки проверены тут.")
            # except Exception as e:
            # bot.reply_to(message, f"Произошла ошибка во время обработки: {e}")
            else:
                bot.reply_to(message, "Обработка отменена.")

    else:
        bot.reply_to(message, "Пожалуйста, отправьте файл .csv")


if __name__ == "__main__":
    # print(load_checked())

    bot.polling()