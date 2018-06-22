# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

route_items = ospf_route.split()
route_items = [item.strip('[],') for item in route_items]
route_items.remove('via')

route = {}
route['Protocol'] = 'OSPF'
route['Prefix'] = route_items[1]
route['AD/Metric'] = route_items[2]
route['Next-Hop'] = route_items[3]
route['Last update'] = route_items[4]
route['Outbound Interface'] = route_items[5]

route_template = '''
{0:<22} {1:} 
{2:<22} {3:}
{4:<22} {5:}
{6:<22} {7:}
{8:<22} {9:}
{10:<22} {11:}
'''
print(route_template.format(
'Protocol:', route['Protocol'], 
'Prefix:', route['Prefix'], 
'AD/Metric:', route['AD/Metric'], 
'Next-Hop:', route['Next-Hop'], 
'Last update:', route['Last update'], 
'Outbound Interface:', route['Outbound Interface'])
)
