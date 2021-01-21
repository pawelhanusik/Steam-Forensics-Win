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
        alldata = alldata['UserLocalConfigStore']['friends']

        for friend in alldata:
            if type(alldata[friend]) is dict:
                toAdd = alldata[friend]
                if '' in toAdd:
                    toAdd = toAdd['']
                uids_data[friend] = {
                    'UID': friend
                }
                uids_data[friend].update(toAdd)
        
        data[uid] = uids_data
        '''first = True
        for friend in uids_data:
            if not first:
                print('='*25)
            else:
                first = False
            utils.printAsTable(uids_data[friend])'''
        #utils.printAdvancedTable(uids_data)
    return data
    
