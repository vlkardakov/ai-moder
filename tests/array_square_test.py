import time
import random

# Создание списка
N = 10 ** 2
lst = [random.randint(0,1000) for _ in range(N)]

start = time.time()

def llambda(listr):
    return listr**15
mapped = map(llambda, lst)
print(mapped)
result_map = sum(mapped)
print(result_map)
end = time.time()
print(f"Время выполнения подхода с map и lambda: {end - start} секунд")