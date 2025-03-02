from urllib.parse import urlparse

def get_domain(url):
  return urlparse(url).netloc