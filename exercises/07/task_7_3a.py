# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
mac_line = []
mac_table = []
with open('CAM_table.txt') as src:
    for line in src:
        if line.find('DYNAMIC') != -1:
            mac_line = line.strip().split()
            mac_line.remove('DYNAMIC')
            mac_table.append(mac_line)
mac_table.sort()
for line in mac_table:
    print("{:>4}{:>18}{:>8}".format(line[0], line[1], line[2]))
