#!/usr/bin/env python

from mcni import neutron_buffer, neutron
b = neutron_buffer(20)
for i in range(len(b)):
    n = neutron(r=(1,2,3), v=(4,5,6), s=(7,8), time=9, prob=i)
    b[i] = n

from mcni.neutron_storage import dump
dump(b, 'neutrons.mcvine')
dump(b, '../input-neutrons.mcvine')
