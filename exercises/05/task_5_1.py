#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

network = input('Введите IP-сеть в формате xxx.xxx.xxx.xxx/xx: ')
mask_int = int(network.split('/')[-1])
network = network.split('/')[0]
octet = network.split('.')
mask_str = mask_int*'1'+(32-mask_int)*'0'


template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{4}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:08b} {6:08b} {7:08b} {8:08b}
'''
print(template.format(
int(octet[0]), int(octet[1]), int(octet[2]), int(octet[3]),
mask_int,
int(mask_str[0:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), int(mask_str[24:32], 2)
))
