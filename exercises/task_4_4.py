# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
command1 = command1.split()[-1]
command2 = command2.split()[-1]
vlans1 = command1.split(',')
vlans2 = command2.split(',')
vlans1 = [int(vlans1[i]) for i in range(5)]
vlans2 = [int(vlans2[i]) for i in range(4)]
vlans_intersecton = list(set(vlans1) & set(vlans2))
print(vlans_intersecton)
