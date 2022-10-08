# programa q lea 7 datas de nascimentos e mostre quantas ainda n sao maiores e quantas sao .

import datetime

for j in range(1, 8):
    data = int(input('Em que ano a {} pessoa nasceu: '.format(j)))
    date = datetime.date(data)
    if date >= 20:
        print('q velho')
