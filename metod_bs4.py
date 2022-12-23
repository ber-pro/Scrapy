from bs4 import BeautifulSoup

# .find()
# .find_all('teg',{'class':'text class'})

# .parent()
# .find('teg', text='oromvrm').parent() находит выше стоящий контейнер

# .find_parent() находит все выше стоящие контейнеры
# .find_next_sibling()
# .find_previous_sibling()


import re  # регулярные выражения(поиск по шаблону)


# получения только цифр по шаблону

def get_num(s):
    pattern = r'\d{1,9}'  # из строки выбираем только цифры от 1 до 9
    salary = re.findall(pattern, s)[0]
    print(salary)


def main():
    salary = soup.find_all('')
    text = 'nemvkmvwe'
    salary = re.find_all('div', text=re.compile(text))  # метод поиска по шаблону определенного тега с таким текстом

    # регулярные выражения (pythex)
    # ^  - начало строки
    # $  - конец строки
    # .  - любой символ
    # +  - неограниченное количество вхождений
    # '\d'- цифры
    # '\w'- буквы, цифры, _____
