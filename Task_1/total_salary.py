from pathlib import Path
import math

def sum_avarage(salary):
    suma=sum(salary)
    avarage=suma//len(salary)
    return (suma,avarage)

def int_check(txt_split):
    try:
        check=int(txt_split)
    except ValueError:
        exit(''' Помилка шаблону тексту. У файлі Шаблон має бути наступним:
              Ім'я працівника,Зарплата працівника
              Ім'я працівника,Зарплата працівника
              !!!Зарплата працівника має бути записана цифрами!!!''' )
    return(check)


def total_salary(path):
    try:
        with open(path, 'r',encoding='utf-8') as fh:
            salary=[]
            for txt in fh.readlines():
                txt_split=txt.strip().split(',')
                salary.append(int_check(txt_split[1]))
            return sum_avarage(salary)
    except FileNotFoundError or FileExistsError:
        exit('Ваш файл відсутній або пошкоджений.')


input_inf=Path('./Module_4/Task_1/salary.txt')
total, average = total_salary(input_inf)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

