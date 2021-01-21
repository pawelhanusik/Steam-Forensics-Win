import os
from datetime import datetime

import utils,vdf

def run():
    data = {}
    dataCanWrite = False
    userdata_path = utils.getInstallPath() + '/userdata'
    uids = os.listdir(userdata_path)
    
    first = True
    for uid in uids:
        if not first:
            print('='*25)
        else:
            first = False
        
        filepath = userdata_path + '/' + uid + '/config/localconfig.vdf'
        uids_data = {}

        alldata = vdf.parse(filepath)
        uids_data.update(alldata['UserLocalConfigStore']['streaming_v2'])
        data[uid] = uids_data
    
    return data
    
