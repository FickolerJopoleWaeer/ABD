import requests                     # Импортируем модуль для HTTP-запросов
from collections import defaultdict # Импортируем defaultdict для удобного подсчёта значений

'''
Мальцев Дмитрий, АСУ8-24-1м

Задача 1. Файл mbox.txt содержит метаданные почтового сервера. Мы знаем, что строка 
с адресом автора письма начинается с "From ". Найти адреса всех авторов сообщений и 
найти того из них, кто пишет больше всех писем. 
Исходный файл можно взять по ссылке: http://www.py4inf.com/code/mbox.txt 
'''

def fetch_and_parse_mbox(url):
    запрос = requests.get(url)      # Отправляем GET-запрос по указанному URL
    запрос.raise_for_status()       # Проверяем, что запрос был успешным, иначе выбрасываем исключение
    словарь = defaultdict(int)      # Создаём словарь, где ключ — email, а значение — количество писем
    
    for строка in запрос.text.split('\n'):  # Проходим по строкам загруженного текста
        if строка.startswith("From "):      # Проверяем, начинается ли строка с "From "
            слова = строка.split()          # Разбиваем строку на слова (по пробелам)
            if len(слова) > 1:              # Проверяем, что в строке есть хотя бы два слова (чтобы избежать ошибок)
                email = слова[1]            # Второе слово — это email-адрес отправителя
                словарь[email] += 1         # Увеличиваем счётчик писем для этого email
    return словарь                          # Возвращаем словарь с подсчётом писем для каждого email

# наибольшее количество писем
def find_top_sender(словарь):
    return max(словарь.items(), key=lambda x: x[1]) if словарь else (None, 0)  # Находим email с наибольшим числом писем

url = "http://www.py4inf.com/code/mbox.txt"     # URL файла с письмами
словарь = fetch_and_parse_mbox(url)             # Загружаем и анализируем файл
автор, письма = find_top_sender(словарь)        # Находим самого активного автора

# Выводим количество писем от самого активного автора и его email:
print("Автор с наибольшим количеством писем:", автор)
print("Количество писем:", письма)
# print("Словарь:", словарь) # для проверки
'''
[ Вывод ]

Автор с наибольшим количеством писем: zqian@umich.edu
Количество писем: 195

Словарь: 
{
'stephen.marquard@uct.ac.za': 29, 
'louis@media.berkeley.edu': 24, 
'zqian@umich.edu': 195, 
'rjlowe@iupui.edu': 90, 
'cwen@iupui.edu': 158, 
'gsilver@umich.edu': 28, 
'wagnermr@iupui.edu': 44, 
'antranig@caret.cam.ac.uk': 18, 
'gopal.ramasammycook@gmail.com': 25, 
'david.horwitz@uct.ac.za': 67, 
'ray@media.berkeley.edu': 32, 
'mmmay@indiana.edu': 161, 
'stuart.freeman@et.gatech.edu': 17, 
'tnguyen@iupui.edu': 6, 
'chmaurer@iupui.edu': 111, 
'aaronz@vt.edu': 110, 
'ian@caret.cam.ac.uk': 96, 
'csev@umich.edu': 19, 
'jimeng@umich.edu': 93, 
'josrodri@iupui.edu': 28, 
'knoop@umich.edu': 5, 
'bkirschn@umich.edu': 27, 
'dlhaines@umich.edu': 84, 
'hu2@iupui.edu': 7, 
'sgithens@caret.cam.ac.uk': 43, 
'arwhyte@umich.edu': 27, 
'gbhatnag@umich.edu': 3, 
'gjthomas@iupui.edu': 44, 
'a.fish@lancaster.ac.uk': 14, 
'ajpoland@iupui.edu': 48, 
'lance@indiana.edu': 8, 
'ssmail@indiana.edu': 5, 
'jlrenfro@ucdavis.edu': 1, 
'nuno@ufp.pt': 28, 
'zach.thomas@txstate.edu': 17, 
'ktsao@stanford.edu': 12, 
'ostermmg@whitman.edu': 17, 
'john.ellis@rsmart.com': 8, 
'jleasia@umich.edu': 2, 
'ggolden@umich.edu': 8, 
'thoppaymallika@fhda.edu': 1, 
'kimsooil@bu.edu': 14, 
'bahollad@indiana.edu': 4, 
'jzaremba@unicon.net': 9, 
'mbreuker@loi.nl': 9, 
'colin.clark@utoronto.ca': 1
}
'''