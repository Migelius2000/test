# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif 'switchport mode access' in line:
                ports_dict['access'][interface]=1
            elif 'switchport access vlan' in line:
                vlan = line.split()[-1]
                ports_dict['access'][interface]=int(vlan)
            elif 'trunk allowed vlan' in line:
                vlans_str = line.split()[-1]
                vlans = [int(i) for i in vlans_str.split(',')]
                ports_dict['trunk'][interface]=vlans            
    return ports_dict

print(get_int_vlan_map('config_sw2.txt')['access'])
print(get_int_vlan_map('config_sw2.txt')['trunk'])
