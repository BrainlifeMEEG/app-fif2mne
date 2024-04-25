# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# set up environment
import os
import json
import mne

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)


fname = config['fif']


# COPY THE METADATA CHANNELS.TSV, COORDSYSTEM, ETC ==============================


raw = mne.io.read_raw_fif(fname)

# save mne/raw
raw.save(os.path.join('out_dir','raw.fif'))

# create a product.json file to show info in the process output
info = raw.info
dict_json_product = {'brainlife': []}

info = str(info)
dict_json_product['brainlife'].append({'type': 'info', 'msg': info})

with open('product.json', 'w') as outfile:
    json.dump(dict_json_product, outfile)