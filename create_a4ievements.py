#################Єбаут#################################################
'''
Даний скрипт допомагає з генерацією файла ачівок для Steam з україською локалізацією
Наклацаний (не)від всієї душі Death_Hunter'ом
'''
import re
#################Шляхи до файлів#######################################
#Оригінальний файл ачівок який знаходиться в 
#windows: <Папка встановлення Steam>\appcache\stats\
#linux: <Папка бібліотеки Steam>\appcache\stats\
original_a4ieve_file = r"UserGameStatsSchema_460790.bin"

#Шлях до файлу (або той же файл як в моєму випадку) в котрому зберегти модифіковані дані,
#потім цей файл перейменувати згідно оригінального та замінити в папці вказаній вище
extract_file = original_a4ieve_file

#Текстовий файл з перекладеними ачівками
trans_file = r"ачівки.txt"
#######################################################################
raw_data = open(original_a4ieve_file, 'r' , encoding='utf-8').read()
trans_base = open(trans_file, 'r' , encoding='utf-8').read()
trans_list = [j for v in [y.split('\n') for y in trans_base.split('\n\n')] for j in v]

pat = 'german\x00.*?(?=\x00)'                                   #Не звертайте уваги на це, це НЕ заміна німецької, це для того (див. ряд. 23)

def tr (pat=pat, raw_data=raw_data, trans_list=trans_list):
    mod_data = raw_data
    offsets = [g for g in re.finditer(pat, raw_data)]
    for o, u in enumerate(offsets):
        mtch = u.group()
        insrt = f"{mtch}\x00\x01ukrainian\x00{trans_list[o]}"   #щоб після німецької українську вставити, бо англійська (в деяких іграх) перед токеном і хз шо буде якшо після англ вставити
        mod_data = mod_data.replace(mtch, insrt)
    return mod_data
#################Збереження змін не забудьте про бекап####################
with open(extract_file, 'w', encoding='utf-8') as ff:
	ff.write(tr())