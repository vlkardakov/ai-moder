import tldextract
from urllib.parse import urlparse

def get_domain(url):
  """
  Извлекает регистрационный домен (например, google.com) из URL.

  Аргументы:
      url: URL для обработки.

  Возвращает:
      Регистрационный домен (строка) или None, если не удалось извлечь.
  """
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