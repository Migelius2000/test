# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(cfg_file):
    with open(cfg_file) as f:
        ports_dict={}
        ports_dict['access']={}
        ports_dict['trunk']={}
        for line in f:
            if 'interface FastEthernet' in line:
                interface = line.split()[-1]
            elif 'switchport access vlan' in line:
                vlan = line.split()[-1]
                ports_dict['access'][interface]=int(vlan)
            elif 'trunk allowed vlan' in line:
                vlans_str = line.split()[-1]
                vlans = [int(i) for i in vlans_str.split(',')]
                ports_dict['trunk'][interface]=vlans            
    return ports_dict

print(get_int_vlan_map('config_sw1.txt')['access'])
print(get_int_vlan_map('config_sw1.txt')['trunk'])
