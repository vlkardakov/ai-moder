import time
import urllib.parse

def filter_phishing_sites(cursor, longurl, title, authorip):
    """
    Фильтрует фишинговые сайты на основе различных проверок по черным и белым спискам.
    Добавлена проверка на SEO статус.
    Оптимизированная версия без referer, ydb, yourls_site, title_for_check, key_for_check и source.

    Аргументы:
        cursor: Курсор базы данных для выполнения SQL-запросов.
        longurl: URL для проверки.
        title: Заголовок веб-страницы.
        authorip: IP-адрес автора.
        key: Ключ короткой ссылки.
        author_country: Код страны автора.

    Возвращает:
        tuple: (статус, причина), где статус может быть 'scam' (скам), 'whitelisted' (белый список),
               'seo' (сео), или 'safe' (безопасный), и reason (причина) - строка, объясняющая статус, или пустая строка, если безопасно.
               Статус 'seo' означает, что ссылка безопасна, но может быть помечена как 'seo' для дальнейшей обработки (например, изменения заголовка).
    """
    white_listed = False
    phishing = False
    ip_checked = False
    scam_reason = ''
    scam_reason_title = ''
    title_was_changed = False # Добавлена переменная для отслеживания изменения title (для SEO, пока всегда False в этой версии)

    ltd = 250
    longurl_no_apostrof = longurl.replace("'", "!").replace("#", "!")
    longurl_ltd = longurl_no_apostrof[:ltd]

    cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (longurl_ltd,))
    check_black_domain = cursor.fetchone()

    if check_black_domain:
        phishing = True
        scam_reason_title = 'Full URL'
    else:
        cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (longurl_ltd,))
        check_white_domain = cursor.fetchone()
        if check_white_domain:
            white_listed = True
        else:
            parse = urllib.parse.urlparse(longurl_no_apostrof)
            full_domain_name = parse.netloc
            path_of_url = parse.path
            query_of_url = parse.query
            if full_domain_name.startswith('www.'):
                full_domain_name = full_domain_name[4:]


            domain_parts = full_domain_name.split('.')
            domain_parts.reverse()
            domain_part_1 = domain_parts[0] if len(domain_parts) > 0 else ''
            domain_part_2 = domain_parts[1] if len(domain_parts) > 1 else ''
            domain_part_3 = domain_parts[2] if len(domain_parts) > 2 else ''
            domain_part_4 = domain_parts[3] if len(domain_parts) > 3 else ''
            domain_part_5 = domain_parts[4] if len(domain_parts) > 4 else ''
            domain_part_6 = domain_parts[5] if len(domain_parts) > 5 else ''
            domain_part_7 = domain_parts[6] if len(domain_parts) > 6 else ''
            domain_part_8 = domain_parts[7] if len(domain_parts) > 7 else ''
            domain_part_9 = domain_parts[8] if len(domain_parts) > 8 else ''

            domain_level_2 = f"{domain_part_2}.{domain_part_1}" if domain_part_2 and domain_part_1 else full_domain_name # Обработка случаев с однокомпонентными доменами
            full_domain_name_ltd = full_domain_name[:ltd]

            cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (full_domain_name_ltd,))
            check_black_domain = cursor.fetchone()
            if check_black_domain:
                phishing = True
                scam_reason_title = full_domain_name_ltd
            else:
                cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (full_domain_name_ltd,))
                check_white_domain = cursor.fetchone()
                if check_white_domain:
                    white_listed = True
                else:
                    if domain_level_2 != full_domain_name:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_level_2,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_level_2
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_level_2,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    if not phishing and not white_listed:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_part_2,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_part_2
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_part_2,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    if not phishing and not white_listed and domain_part_3 and (domain_part_2 == 'com' or domain_part_2 == 'co'):
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_part_3,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_part_3
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_part_3,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    domain_prefix = f"{domain_part_3}.{domain_level_2}"
                    if not phishing and not white_listed and domain_part_3:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_prefix,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_prefix
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_prefix,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    domain_prefix = f"{domain_part_4}.{domain_prefix}"
                    if not phishing and not white_listed and domain_part_4:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_prefix,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_prefix
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_prefix,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    domain_prefix = f"{domain_part_5}.{domain_prefix}"
                    if not phishing and not white_listed and domain_part_5:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_prefix,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_prefix
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_prefix,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    domain_prefix = f"{domain_part_6}.{domain_prefix}"
                    if not phishing and not white_listed and domain_part_6:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_prefix,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_prefix
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_prefix,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    domain_prefix = f"{domain_part_7}.{domain_prefix}"
                    if not phishing and not white_listed and domain_part_7:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_prefix,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_prefix
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_prefix,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    domain_prefix = f"{domain_part_8}.{domain_prefix}"
                    if not phishing and not white_listed and domain_part_8:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_prefix,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_prefix
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_prefix,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True

                    domain_prefix = f"{domain_part_9}.{domain_prefix}"
                    if not phishing and not white_listed and domain_part_9:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (domain_prefix,))
                        check_black_domain = cursor.fetchone()
                        if check_black_domain:
                            phishing = True
                            scam_reason_title = domain_prefix
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (domain_prefix,))
                            check_white_domain = cursor.fetchone()
                            if check_white_domain:
                                white_listed = True


                    if not phishing and not white_listed:
                        title_ltd = title[:ltd]
                        title_ltd = title_ltd.replace("'", "#")
                        cursor.execute("SELECT * FROM black_title WHERE title = %s", (title_ltd,))
                        check_black_title = cursor.fetchone()
                        if check_black_title:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = title_ltd

                    if not phishing and not white_listed and path_of_url and path_of_url != '/':
                        check_path = path_of_url[1:5] # до индекса 4, итого 4 символа
                        cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path,))
                        check_black_path = cursor.fetchone()
                        if check_black_path:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = check_path
                        else:
                            if check_path == 'maps':
                                google_domains = ['google', 'goo']
                                top_level_domains_for_google = ['com', 'co', 'gl']
                                domain_part_2_check = domain_part_2.lower()
                                domain_part_3_check = domain_part_3.lower()

                                if (domain_part_2_check in google_domains) or \
                                   (domain_part_3_check == 'google' and (domain_part_2_check in top_level_domains_for_google)) or \
                                   (domain_part_2_check == 'goo' and domain_part_1 == 'gl'):
                                    white_listed = True

                    if not phishing and not white_listed and path_of_url and path_of_url != '/':
                        check_path = path_of_url[1:9] # до индекса 8, итого 8 символов
                        cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path,))
                        check_black_path = cursor.fetchone()
                        if check_black_path:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = check_path

                    if not phishing and not white_listed and path_of_url and path_of_url != '/':
                        check_path = path_of_url[1:7] # до индекса 6, итого 6 символов
                        cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path,))
                        check_black_path = cursor.fetchone()
                        if check_black_path:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = check_path

                    if not phishing and not white_listed and query_of_url:
                        query_parts = query_of_url.split('=', 1) # Разделить только один раз по первому '='
                        query_part_1 = query_parts[0] if query_parts else ''
                        query_part_2 = query_parts[1] if len(query_parts) > 1 else ''

                        if query_part_1:
                            check_path_parameter = query_part_1[:4]
                            cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_parameter,))
                            check_black_path = cursor.fetchone()
                            if check_black_path:
                                phishing = True
                                scam_reason = 'Check '
                                scam_reason_title = check_path_parameter
                            else:
                                check_path_parameter = query_part_1[:8]
                                cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_parameter,))
                                check_black_path = cursor.fetchone()
                                if check_black_path:
                                    phishing = True
                                    scam_reason = 'Check '
                                    scam_reason_title = check_path_parameter

                        if not phishing and not white_listed and query_part_2:
                            check_path_parameter = query_part_2[:4]
                            cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_parameter,))
                            check_black_path = cursor.fetchone()
                            if check_black_path:
                                phishing = True
                                scam_reason = 'Check '
                                scam_reason_title = check_path_parameter
                            else:
                                check_path_parameter = query_part_2[:8]
                                cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_parameter,))
                                check_black_path = cursor.fetchone()
                                if check_black_path:
                                    phishing = True
                                    scam_reason = 'Check '
                                    scam_reason_title = check_path_parameter

                    if not phishing and not white_listed and domain_part_3 and domain_part_2 != 'com' and domain_part_2 != 'co':
                        check_path_domain_part_3 = domain_part_3[:8]
                        cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_domain_part_3,))
                        check_black_path = cursor.fetchone()
                        if check_black_path:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = check_path_domain_part_3

                    if not phishing and not white_listed and domain_part_4:
                        check_path_domain_part_4 = domain_part_4[:8]
                        cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_domain_part_4,))
                        check_black_path = cursor.fetchone()
                        if check_black_path:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = check_path_domain_part_4

                    if not phishing and not white_listed and domain_part_5:
                        check_path_domain_part_5 = domain_part_5[:8]
                        cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_domain_part_5,))
                        check_black_path = cursor.fetchone()
                        if check_black_path:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = check_path_domain_part_5

                    if not phishing and not white_listed and domain_part_6:
                        check_path_domain_part_6 = domain_part_6[:8]
                        cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_domain_part_6,))
                        check_black_path = cursor.fetchone()
                        if check_black_path:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = check_path_domain_part_6

                    if not phishing and not white_listed and domain_part_7:
                        check_path_domain_part_7 = domain_part_7[:8]
                        cursor.execute("SELECT * FROM black_path WHERE path = %s", (check_path_domain_part_7,))
                        check_black_path = cursor.fetchone()
                        if check_black_path:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = check_path_domain_part_7


                    if not phishing and not white_listed:
                        substring_checks = [
                            'amaz0n', '://192.168.', '.byethost', 'shrink', 'url.', 'shrt',
                            '.exe', 'banque', ' anal ', 'creampie', 'erection', 'femboy', ' gay ',
                            'penis', 'testicles', 'sissy', 'sex', 'fuck', ' ass ', 'секс', 'порно'
                        ]
                        substring_checks_lower_case = [s.lower() for s in substring_checks] # Для регистронезависимой проверки заголовка
                        longurl_lower = longurl.lower()
                        title_lower = title.lower() if title else "" # Используем title напрямую

                        if any(sub in longurl_lower for sub in ['==', 'freefir', '478x84579', 'garena', 'porn']) or any(sub in title_lower for sub in ['garena', 'freefir', 'free fir', 'porn', 'pubg'] + substring_checks_lower_case) or domain_part_1 == 'onion':
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = '== amaz0n freefir ...'


                    if not phishing and not white_listed and authorip:
                        cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (authorip,))
                        check_black_IP = cursor.fetchone()
                        ip_checked = True
                        if check_black_IP:
                            phishing = True
                            scam_reason = 'Check '
                            scam_reason_title = authorip
                        else:
                            cursor.execute("SELECT * FROM white_domain WHERE domain = %s", (authorip,))
                            check_white_IP = cursor.fetchone()
                            if check_white_IP:
                                white_listed = True

    if phishing:
        if not ip_checked:
            cursor.execute("SELECT * FROM black_domain WHERE domain = %s", (authorip,))
            check_black_IP = cursor.fetchone()
        if not check_black_IP:
            scam_reason = scam_reason + ' IP '



    if phishing:
        return "scam", f"Фишинг обнаружен: {scam_reason} - {scam_reason_title}"
    elif white_listed:
        return "whitelisted", "URL в белом списке"
    elif not phishing and not white_listed: # Если не фишинг и не белый список, то помечаем как "seo"
        return "seo", "Безопасная ссылка, помечена как SEO" #  Здесь можно добавить более детальную причину SEO, если нужно
    else: # Добавлено для явной обработки случая, когда не фишинг и не белый список и не SEO (если захотите добавить более сложную логику для SEO)
        return "safe", "" # Безопасная ссылка, не помечена как SEO


# Пример использования (предполагается, что у вас есть подключение к базе данных и курсор):
# status, reason = filter_phishing_sites(cursor, longurl, title, authorip, key, author_country)
# print(f"Статус: {status}, Причина: {reason}")