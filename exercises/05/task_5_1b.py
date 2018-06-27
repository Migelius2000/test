#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ip = argv[1]
mask_int = int(ip.split('/')[-1])
ip = ip.split('/')[0]
octet = ip.split('.')
mask_str = mask_int*'1'+(32-mask_int)*'0'
ip_bin = '{0:08b}{0:08b}{0:08b}{0:08b}'.format(int(octet[0]), int(octet[1]), int(octet[2]), int(octet[3]))
network = ip_bin[0:(mask_int)] + (32-mask_int)*'0'

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
int(network[0:8], 2), int(network[8:16], 2), int(network[16:24], 2), int(network[24:32], 2),
mask_int,
int(mask_str[0:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), int(mask_str[24:32], 2)
))
