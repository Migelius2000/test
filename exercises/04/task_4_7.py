# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

mac_octet = MAC.split(':')

print('{:b}{:b}{:b}'.format(int(mac_octet[0], 16), int(mac_octet[1], 16), int(mac_octet[2], 16)))
