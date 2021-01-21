from datetime import datetime

import utils,vdf

def run():
    data = []
    dataCanWrite = False
    filepath = utils.getInstallPath() + '/config/loginusers.vdf'
    
    data = vdf.parse(filepath)
    for u in data['users']:
        #add converted timestamp
        if 'Timestamp' in data['users'][u]:
            data['users'][u]['Timestamp'] += ' (' + datetime.utcfromtimestamp(int(data['users'][u]['Timestamp'])).strftime('%Y-%m-%d %H:%M:%S') + ')'
    #return results
    return data
