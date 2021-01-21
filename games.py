import os, sys
from datetime import datetime
import urllib.request

import utils,vdf

def run():
    fetchGameNames = False

    ret = {}
    userdata_path = utils.getInstallPath() + '/userdata'
    uids = os.listdir(userdata_path)
    
    #Ask
    tmp_fetchGameNames = input('Fetch game names from the internet? [y/N] (default: no) ')
    if tmp_fetchGameNames == 'y' or tmp_fetchGameNames == 'Y':
        fetchGameNames = True
    #End asking

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
        i = 0
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
            if fetchGameNames and 'GameID' in data[gameID]:
                print('Fetching game names from the internet {}/{}'.format(i, len(alldata)), file=sys.stderr, end="\r")
                i += 1
                with urllib.request.urlopen(f'https://store.steampowered.com/app/{gameID}/') as response:
                    html = response.read()
                    html = html.decode('utf-8')
                    a = html.find('<title>') + 7
                    b = html.find('</title>')
                    title = html[a:b]
                    if title.find(' on Steam') == len(title) - 9:
                        title = title[:-9]
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
