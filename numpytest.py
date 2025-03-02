import numpy as np
import time
from linkprocessing import save_checked, load_checked
while True:
    try:
        input()

        print('начали')
        time1 = time.time()
        checked = load_checked()
        print(np.append(checked, 'hothinginteresting.com'))
        print(len(checked))
        print(type(checked))
        print(f'заняло {time.time() - time1}')
    except KeyboardInterrupt:
        print('Пока!')
        exit()
