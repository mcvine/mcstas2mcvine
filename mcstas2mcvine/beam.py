# -*- python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

"""
In mcstas, virtual_input and virtual_output read and write text files for neutrons.
The columsn are: p x y z vx vy vz t sx sy sz

In mcvine, a neutron storage can be converted to a numpy array. The columns are:
x y z vx vy vz s1 s2 t p

"""

import numpy as np, os
from mcni import neutron_storage as ns

def mcvine2mcstas(inpath, outpath):
    arr = ns.readneutrons_asnpyarr(inpath)
    N = len(arr)
    newarr = np.zeros((N, 11), dtype=float)
    newarr[:, list(range(10))] = arr[:, [9, 0,1,2, 3,4,5, 8, 6,7]]
    np.savetxt(outpath, newarr)
    return


def mcstas2mcvine(inpath, outpath):
    arr = np.loadtxt(inpath)
    N = len(arr)
    newarr = np.zeros((N, 10), dtype=float)
    newarr[:, list(range(10))] = arr[:, [1,2,3, 4,5,6, 8,9, 7, 0]]
    neutrons = ns.neutrons_from_npyarr(newarr)
    ns.dump(neutrons, outpath)
    return

# End of file
