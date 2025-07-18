#################Єбаут#################################################
'''
Даний скрипт допомагає з видобутком ачівок для Steam для подальшої українізації
Наклацаний (не)від всієї душі Death_Hunter'ом
'''
import re
#################Шляхи до файлів#######################################
#Оригінальний файл ачівок який знаходиться в 
#windows: <Папка встановлення Steam>\appcache\stats\
#linux: <Папка бібліотеки Steam>\appcache\stats\
#копійнути в робочу папку
orig_a4ieve_file = r"UserGameStatsSchema_460790.bin"

#Текстовий файл з ачівками які треба перекласти, щоб потім заюзати інший скрипт
trans_file = r"ачівки.txt"
#######################################################################
raw_data = open(orig_a4ieve_file, 'r' , encoding='utf-8').read()

pat = '(?<=english\x00).*?(?=\x00\x01)'

def rt(pat=pat, raw_data=raw_data):
    string = ''
    for o, i in enumerate(re.findall(pat, raw_data)):
        string += f'{i}\n'
        if o % 2 == 1: string += '\n'
    return string

with open(trans_file, 'w', encoding='utf-8') as ff:
	ff.write(rt())