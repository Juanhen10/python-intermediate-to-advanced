# Criando data com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano,mês, dia, horas, minuto, segundo)
# datetime.striptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
# data = datetime(2022, 4, 20, 7, 49, 23)
import os
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pytz import timezone

os.system('cls')
# print(data)

data_now = datetime.now()
print(data_now.timestamp())
print(data_now.fromtimestamp(1676305568.178664))

print()
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta = timedelta(days=10)
delta = relativedelta(data_fim, data_inicio)
print()
print(delta)
print(data_fim + relativedelta(seconds=59))
delta = data_fim - data_inicio
print()
print(delta.days, delta.seconds, delta.max)
print(delta.total_seconds())
print()
print(data_fim > data_inicio)
print(data_inicio > data_fim)
print(data_fim == data_inicio)
