import os, sys
from datetime import datetime
import urllib.request

import utils,vdf

def run():
    ret = {}
    userdata_path = utils.getInstallPath() + '/userdata'
    uids = os.listdir(userdata_path)

    first = True
    for uid in uids:
        if not first:
            print('='*50)
        else:
            first = False
        
        filepath = userdata_path + '/' + uid + '/config/localconfig.vdf'
        data = {}

        alldata = vdf.parse(filepath)
        alldata = alldata['UserLocalConfigStore']['Software']['Valve']['Steam']['Apps']
        for gameID in alldata:
            if gameID == '':
                continue
            data[gameID] = {
                'GameID': gameID
            }
            data[gameID].update(alldata[gameID])

            #===
            if 'LastPlayed' in data[gameID]:
                data[gameID]['LastPlayed'] += ' (' + datetime.utcfromtimestamp(int(data[gameID]['LastPlayed'])).strftime('%Y-%m-%d %H:%M:%S') + ')'
            if 'Playtime' in data[gameID]:
                playtime = int(data[gameID]['Playtime'])
                data[gameID]['Playtime'] += ' ( {0}h {1}m )'.format(playtime//60, playtime%60)
            if 'GameID' in data[gameID]:
                title = utils.fetchGameName(gameID)
                if title != None:
                    data[gameID]['GameID'] += f' ( {title} )'
                    
            #===

        ret[uid] = data
        #utils.printAdvancedTable(data)
        '''first = True
        for gameID in data:
            if not first:
                print('='*25)
            else:
                first = False
            utils.printAsTable(data[gameID])'''
    
    return ret
