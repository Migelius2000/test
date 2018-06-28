#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_addr = input('Введите IP-адрес в формате xxx.xxx.xxx.xxx: ')
octets = ip_addr.split('.')
while True:
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
        for i in octets:
            if i<0 or i>255:
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
            break
        break
    ip_addr = input('Введите IP-адрес в формате xxx.xxx.xxx.xxx: ')
