import sys
from pathlib import Path
from colorama import Fore, Style

def directory_structure(directory: Path, indentation: str=''):
    try:
        iterations = sorted(directory.iterdir(), key=lambda i: (i.is_file(), i.name.lower()))
    except PermissionError:
        print(f'{Fore.RED}[Access Denied] {directory}{Style.RESET_ALL}')
        return 0
    
    for iteration in iterations:
        if iteration.is_dir():
            print(f'    {Fore.BLUE}📦 [Directory] {iteration.name}{Style.RESET_ALL}')
            directory_structure(iteration, indentation + '    ')
        elif iteration.is_file():
            print(f'    {indentation}{Fore.RED}📜 [File] {iteration.name}{Style.RESET_ALL}')

def main():
    if len(sys.argv) != 2:
        print(f'{Fore.RED}[ERROR] You have to provide two arguments: [script] [directory]!')
        sys.exit(-1)
    
    directory=Path(sys.argv[1])

    if not directory.exists():
        print(f'{Fore.RED}[ERROR] Path {directory} doesn\'t exist!{Style.RESET_ALL}')
        sys.exit(-1)
    
    if not directory.is_dir():
        print(f'{Fore.RED}[ERROR] Path {directory} isn\'t a directory!{Style.RESET_ALL}')
        sys.exit(-1)
    
    print(f'{Fore.CYAN}📦 [Directory] {directory.name}{Style.RESET_ALL}')
    directory_structure(directory)

if __name__ == "__main__":
    main()