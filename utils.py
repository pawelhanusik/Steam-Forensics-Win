import os, sys
import urllib.request
import socket

install_path = "C:/Program Files (x86)/Steam"
appdata_path = os.getenv('LOCALAPPDATA') + "/Steam/"

use_default_install = None
use_default_appdata = None
fetch_game_names = None
fetch_user_names = None

gameNamesCache = {}
userNamesCache = {}

def getInstallPath():
    global use_default_install
    global install_path

    if use_default_install == None:
        try:
            use_default_install = input(f'Use default Steam install path? ({install_path}) [Y/n] (default: Y): ')
        except KeyboardInterrupt:
            exit()
        if len(use_default_install) > 0 and ( use_default_install[0] == 'n' or use_default_install[0] == 'N' ):
            install_path = input('Input Steam install path: ')
    
    return install_path

def getAppdataPath():
    global use_default_appdata
    global appdata_path

    if use_default_appdata == None:
        try:
            use_default_appdata = input(f'Use default Steam appdata path? ({appdata_path}) [Y/n] (default: Y): ')
        except KeyboardInterrupt:
            exit()
        if len(use_default_appdata) > 0 and ( use_default_appdata[0] == 'n' or use_default_appdata[0] == 'N' ):
            appdata_path = input('Input Steam appdata path: ')
    return appdata_path

def fetchGameName(gameID):
    global fetch_game_names
    global gameNamesCache

    if fetch_game_names == None:
        try:
            tmp_fetchGameNames = input('Fetch game names from the internet? [Y/n] (default: yes) ')
        except KeyboardInterrupt:
            exit()
        if len(tmp_fetchGameNames) > 0 and (tmp_fetchGameNames[0] == 'n' or tmp_fetchGameNames[0] == 'N'):
            fetch_game_names = False
        else:
            fetch_game_names = True
    
    if fetch_game_names == False:
        return None

    if gameID in gameNamesCache:
        return gameNamesCache[gameID]
    
    title = None
    
    info2print = f'Fetching game name of {gameID} from the internet...'
    print(info2print, file=sys.stderr, end="\r")
    try:
        timeouts = [15, 20, 40]
        for i in range(0, 3):
            try:
                with urllib.request.urlopen(f'https://store.steampowered.com/app/{gameID}/', timeout=timeouts[i]) as response:
                    html = response.read()
                    html = html.decode('utf-8')
                    #a = html.find('<title>') + 7
                    #b = html.find('</title>')
                    a = html.find('<div class="apphub_AppName">')
                    if a == -1:
                        break
                    a += 28
                    b = html.find('</div>', a)
                    title = html[a:b]
                    #if title.find(' on Steam') == len(title) - 9:
                    #    title = title[:-9]
                    break
            except socket.timeout:
                pass
    except KeyboardInterrupt:
        print('', file=sys.stderr)
        print('Aborted', file=sys.stderr)
        tmp_cont = input('Continue running? [Y/n] (default: y): ')
        if len(tmp_cont) > 0 and (tmp_cont[0] == 'n' or tmp_cont[0] == 'N'):
            exit()
    print(' '*len(info2print), end='\r')
    
    if title != None:
        gameNamesCache[gameID] = title
    return title

def fetchUserName(userID):
    global fetch_user_names
    global userNamesCache

    if fetch_user_names == None:
        try:
            tmp_fetchUserNames = input('Fetch user names from the internet? [Y/n] (default: yes) ')
        except KeyboardInterrupt:
            exit()
        if len(tmp_fetchUserNames) > 0 and (tmp_fetchUserNames[0] == 'n' or tmp_fetchUserNames[0] == 'N'):
            fetch_user_names = False
        else:
            fetch_user_names = True
    
    if fetch_user_names == False:
        return None

    if userID in userNamesCache:
        return userNamesCache[userID]
    
    username = None
    
    info2print = f'Fetching username of {userID} from the internet...'
    print(info2print, file=sys.stderr, end="\r")
    try:
        with urllib.request.urlopen(f'https://steamcommunity.com/profiles/{userID}/') as response:
            html = response.read()
            html = html.decode('utf-8')
            a = html.find('<span class="actual_persona_name">')
            if a != -1:                
                a += 34
                b = html.find('</span>', a)
                username = html[a:b]
    except KeyboardInterrupt:
        print('', file=sys.stderr)
        print('Aborted', file=sys.stderr)
        tmp_cont = input('Continue running? [Y/n] (default: y): ')
        if len(tmp_cont) > 0 and (tmp_cont[0] == 'n' or tmp_cont[0] == 'N'):
            exit()
    print(' '*len(info2print), end='\r')
    
    if username != None:
        userNamesCache[userID] = username
    return username