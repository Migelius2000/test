# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

int_mode = input('Введите режим интерфейса (trunk, access): ')
int_type = input('Введите номер и тип  интерфейса (вида Gi0/1): ')
mode = {'access': 'Введите номер VLAN: ', 'trunk': 'Введите разрешеные VLAN: '}
int_vlan = input(mode[int_mode])


access = '\n'.join(access_template).format(int_vlan)
trunk = '\n'.join(trunk_template).format(int_vlan)
interface = {'access':access, 'trunk':trunk}

print('\ninterface', int_type)
print(interface.get(int_mode))
