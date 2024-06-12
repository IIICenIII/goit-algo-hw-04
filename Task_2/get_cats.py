from pathlib import Path

def get_cats_info(path):
    try:
        with open(path,'r',encoding='utf-8') as fh:
            cats_list=[]
            for indir in fh.readlines():
                dir_split=indir.strip().split(',')
                cats_list.append({'id':dir_split[0],'name':dir_split[1],'age':dir_split[2]})
            return cats_list

    except FileNotFoundError or FileExistsError:
        exit('Файл не знайдено або файл пошкоджений')

input_inf=Path('./Module_4/Task_2/cats.txt')
cats_info = get_cats_info(input_inf)
print(cats_info)
