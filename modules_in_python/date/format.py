# datetime.strftime('DATA','FORMATO')
# https://docs.python.org/3/library/datetime.html
import os
from datetime import datetime

os.system('cls')

fmt = '%d/%m/%Y'
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt))
print(data.strftime("%d/%m/%Y"))
print(data.strftime("%d/%m/%Y %H:%M"))
print(data.strftime("%d/%m/%Y %H:%M:%S"))
print(data.strftime("%Y"))
