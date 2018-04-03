#!/usr/bin/env python

import os, numpy as np

def test1():
    # create mcvine input neutrons
    cmd = 'cd mcvine-create-neutrons; ./dump.py'
    if os.system(cmd):
        raise RuntimeError("%s failed" % cmd)
    # convert from mcvine to mcstas
    from mcstas2mcvine.beam import mcvine2mcstas, mcstas2mcvine
    mcvine2mcstas('input-neutrons.mcvine', 'output-neutrons.mcstas')
    # run through virtual_input and virtual_output inside mcstas
    cmd = 'cd ./test-mcvine2mcstas-output/; ./build.sh; ./run-test.sh'
    if os.system(cmd):
        raise RuntimeError("%s failed" % cmd)
    # convert from mcstas to mcvine
    mcstas2mcvine('test-mcvine2mcstas-output/beam-copy.dat', 'output-neutrons.mcvine')
    # load and verify
    from mcni.neutron_storage import readneutrons_asnpyarr
    ns1 = readneutrons_asnpyarr('input-neutrons.mcvine')
    ns2 = readneutrons_asnpyarr('output-neutrons.mcvine')
    assert np.allclose(ns1, ns2)
    return


if __name__ == '__main__': test1()
