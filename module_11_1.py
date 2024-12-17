import requests
import pandas
# requests
r = requests.get('https://urban-university.ru')
print(r.content) # получение содержимого страницы в байтовом виде
print(r.status_code) # получение статуса кода (в нашем случае 200, что хорошо)
print(r)
print(r.text) # получение содержимого страницы в строковом виде
print(r.headers) # Заголовки в ответе; вывод информации о сервере, дате и кодировки

# pandas
dict = {'Месяцы' : ['Сентябрь', 'Октябрь', "Ноябрь", "Декабрь"],
        'Количество отработанных часов' : [60, 196, 144, 184],
        "Выручка" : ["242 тыс.", "396 тыс.", "351 тыс.", "381 тыс."]}
data_frame = pandas.DataFrame(dict)
print(data_frame) # создание таблицы данных, взятых из словаря
print(data_frame.dtypes) # вывод типа данных
print(data_frame.describe()) # выводы по значениям