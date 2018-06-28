#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip_addr = input('Введите IP-адрес в формате xxx.xxx.xxx.xxx: ')
octets = ip_addr.split('.')
try:
    octets[0] = int(octets[0])
    octets[1] = int(octets[1])
    octets[2] = int(octets[2])
    octets[3] = int(octets[3])
except ValueError:
    print('Incorrect IPv4 address')
except IndexError:
    print('Incorrect IPv4 address')
else:
    if octets[0]<0 or octets[0]>255 or octets[1]<0 or octets[1]>255 or octets[2]<0 or octets[2]>255 or octets[3]<0 or octets[3]>255:
        print('Incorrect IPv4 address')
    else:
        if octets[0] >= 1 and octets[0] <= 223:
            print('unicast')
        elif octets[0] >= 224 and octets[0] <= 239:
            print('multicast')
        elif ip_addr == '255.255.255.255':
            print('local broadcast')
        elif ip_addr == '0.0.0.0' :
            print('unassigned')
        else:
            print('unused')
