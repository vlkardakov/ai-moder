import numpy as np

checked_domains = np.array([], dtype=str)

while True:
    line = input("Введите строку (или 'exit' для завершения): ")
    if line == 'exit':
        break

    if line not in checked_domains:
        checked_domains = np.append(checked_domains, line)
        print("YES")
    else:
        print("PASS")

print("Проверенные строки:", checked_domains)