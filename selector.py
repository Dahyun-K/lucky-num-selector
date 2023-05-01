import random

lotto = []
rnd_num = random.randint(1, 45)

for i in range(6):
    while rnd_num in lotto:
        rnd_num = random.randint(1,45)
    lotto.append(rnd_num)

lotto.sort()
print(f'숫자 6개 선택하기 : {lotto}')
