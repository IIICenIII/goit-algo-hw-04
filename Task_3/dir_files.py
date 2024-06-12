from pathlib import Path,PurePath
from colorama import Fore, Style 
import sys

base=(sys.argv)

def dir_rec(base,num):
    path=Path(base)
    for dir in path.iterdir():
        dir_pure=PurePath(dir)
        if dir.is_dir():
            print(f'{' '*num}{Fore.CYAN}|--{Fore.LIGHTYELLOW_EX}{dir_pure.name}{Style.RESET_ALL}')
            num_n=num+4
            dir_rec(dir,num_n)
        else:
            print(f'{' '*num}{Fore.LIGHTGREEN_EX}|--{Fore.LIGHTMAGENTA_EX}{dir_pure.name}{Style.RESET_ALL}')



def main():
    if len(sys.argv)!=2:
        print('Будь-ласка вкажіть директорію для перевірки')
        return

    base=(sys.argv[1])   
    
    try:
        print('Зчитую дані з:',Fore.BLUE,PurePath(base).name,Style.RESET_ALL)
        dir_rec(base,0)
    except FileNotFoundError:
        print('Помилка директорії. Ваша директорія відсутня.')
        return


if __name__=='__main__':
    main()