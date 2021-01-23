import os
from datetime import datetime
import json
#from datetime import datetime

import utils,vdf

def run():
    data = {}
    userdata_path = utils.getInstallPath() + '/userdata'
    uids = os.listdir(userdata_path)
    
    first = True
    for uid in uids:
        #TODO: remove printing
        '''
        if not first:
            print('='*25)
        else:
            first = False
        '''

        dirpath = userdata_path + '/' + uid + '/config/librarycache'
        uids_data = {}

        games_files = os.listdir(dirpath)
        for game_file in games_files:
            filepath = dirpath + '/' + game_file

            games_achievements = {}
            with open(filepath) as f:
                alldata = json.loads(f.read())
                for x in alldata:
                    if x[0] == 'achievements':
                        #print(x[1]['data']['vecHighlight'])
                        #print('='*25)
                        games_achievements = x[1]['data']['vecHighlight']
                        for gaid in range(len(games_achievements)):
                            if 'rtUnlocked' in games_achievements[gaid]:
                                games_achievements[gaid]['rtUnlocked'] = str(games_achievements[gaid]['rtUnlocked']) + ' (' + datetime.utcfromtimestamp(int(games_achievements[gaid]['rtUnlocked'])).strftime('%Y-%m-%d %H:%M:%S') + ')'
                        break
            gameID = game_file.split('.')[0]
            gameName = utils.fetchGameName(gameID)
            if gameName != None:
                gameID += ' (' + gameName + ')'
            uids_data[gameID] = games_achievements

        data[uid] = uids_data


    return data
    
