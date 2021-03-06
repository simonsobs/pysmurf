import os
import pysmurf.client
import matplotlib.pylab as plt
import numpy as np
import sys

config_file_path='/data/pysmurf_cfg/'

slot=int(sys.argv[1])
epics_prefix = 'smurf_server_s%d'%slot

HB=False

if HB:
    # HB config
    config_file='experiment_nistcmb_srv10_dspv3_cc02-02_hbOnlyBay0.cfg'
else:
    # LB config
    config_file='experiment_nistcmb_srv10_dspv3_cc02-02_lbOnlyBay0.cfg'

config_file=os.path.join(config_file_path,config_file)    

S = pysmurf.client.SmurfControl(epics_root=epics_prefix,cfg_file=config_file,setup=False,make_logfile=False) 

if HB:
    S.set_band_center_mhz(0,6250)
    S.set_band_center_mhz(1,6750)
    S.set_band_center_mhz(2,7250)
    S.set_band_center_mhz(3,7750)
