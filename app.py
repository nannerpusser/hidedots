import os
import re
from rich.console import Console

console = Console()

asciiart = r'''

 _ .-') _                .-') _          ('-. .-.         _ .-') _     ('-.  _  .-')   
( (  OO) )              (  OO) )        ( OO )  /        ( (  OO) )  _(  OO)( \( -O )  
 \     .'_  .-'),-----. /     '._       ,--. ,--.  ,-.-') \     .'_ (,------.,------.  
 ,`'--..._)( OO'  .-.  '|'--...__)      |  | |  |  |  |OO),`'--..._) |  .---'|   /`. ' 
 |  |  \  '/   |  | |  |'--.  .--'      |   .|  |  |  |  \|  |  \  ' |  |    |  /  | | 
 |  |   ' |\_) |  |\|  |   |  |         |       |  |  |(_/|  |   ' |(|  '--. |  |_.' | 
 |  |   / :  \ |  | |  |   |  |         |  .-.  | ,|  |_.'|  |   / : |  .--' |  .  '.' 
 |  '--'  /   `'  '-'  '   |  |         |  | |  |(_|  |   |  '--'  / |  `---.|  |\  \  
 `-------'      `-----'    `--'         `--' `--'  `--'   `-------'  `------'`--' '--' 

'''
console.print(asciiart, style="bold red")

regx = re.compile(r'^\.')
# list to store filename present in current directory
files = []
dirs = []

for file_path in os.listdir('.'):
    if os.path.isfile(os.path.join('.', file_path)) and regx.match(file_path):
        files.append(file_path)


for dir_path in os.listdir('.'):
    if os.path.isdir(os.path.join('.', dir_path)) and regx.match(dir_path):
        dirs.append(dir_path)

print(r"Files and folders present in current directory: " + "\n" + "\n".join(files + dirs))

 
while True:
    user_input = input('Hide files? (y/n): ')
    if user_input == 'y' or user_input == 'Y':
        for file in files:
            os.system(f'attrib +h {file}')
        for dir in dirs:
            os.system(f'attrib +h /d {dir}')
        break

    elif user_input == 'n' or user_input == 'N':
        print('Exiting...')
        break

    else:
        print('Invalid input. Please enter y or n.')
        