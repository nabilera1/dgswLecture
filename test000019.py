# 주사위 놀이
from random import *
# import random
import time

for i in range(5):  # 총 5번의 랜덤 숫자 출력
    print(randint(1, 6))  # random.randint(1,6)
    time.sleep(0.5)  # 0.5초마다
