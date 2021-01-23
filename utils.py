import os, sys
import urllib.request

default_install_path = "C:/Program Files (x86)/Steam"
default_appdata_path = os.getenv('LOCALAPPDATA') + "/Steam/"

use_default_install = None
use_default_appdata = None
fetch_game_names = None
fetch_user_names = None

gameNamesCache = {}
userNamesCache = {}

def getInstallPath():
    global use_default_install
    if use_default_install == None:
        try:
            use_default_install = input(f'Use default Steam install path? ({default_install_path}) [Y/n] (default: Y): ')
        except KeyboardInterrupt:
            exit()
    if len(use_default_install) > 0 and ( use_default_install[0] == 'n' or use_default_install[0] == 'N' ):
        return input('Input Steam install path: ')
    return default_install_path

def getAppdataPath():
    global use_default_appdata
    if use_default_appdata == None:
        try:
            use_default_appdata = input(f'Use default Steam appdata path? ({default_appdata_path}) [Y/n] (default: Y): ')
        except KeyboardInterrupt:
            exit()
    if len(use_default_appdata) > 0 and ( use_default_appdata[0] == 'n' or use_default_appdata[0] == 'N' ):
        return input('Input Steam appdata path: ')
    return default_appdata_path

def fetchGameName(gameID):
    global fetch_game_names
    global gameNamesCache

    if fetch_game_names == None:
        try:
            tmp_fetchGameNames = input('Fetch game names from the internet? [y/N] (default: no) ')
        except KeyboardInterrupt:
            exit()
        if tmp_fetchGameNames == 'y' or tmp_fetchGameNames == 'Y':
            fetch_game_names = True
        else:
            fetch_game_names = False
    
    if fetch_game_names == False:
        return None

    if gameID in gameNamesCache:
        return gameNamesCache[gameID]
    
    title = None
    
    print(f'Fetching game name of {gameID} from the internet...', file=sys.stderr, end="\r")
    try:
        with urllib.request.urlopen(f'https://store.steampowered.com/app/{gameID}/') as response:
            html = response.read()
            html = html.decode('utf-8')
            a = html.find('<title>') + 7
            b = html.find('</title>')
            title = html[a:b]
            if title.find(' on Steam') == len(title) - 9:
                title = title[:-9]
    except KeyboardInterrupt:
        print('', file=sys.stderr)
        print('Aborted', file=sys.stderr)
        tmp_cont = input('Continue running? [Y/n] (default: y): ')
        if len(tmp_cont) > 0 and (tmp_cont[0] == 'n' or tmp_cont[0] == 'N'):
            exit()
    if title != None:
        gameNamesCache[gameID] = title
    return title

def fetchUserName(userID):
    global fetch_user_names
    global userNamesCache

    if fetch_user_names == None:
        try:
            tmp_fetchUserNames = input('Fetch game names from the internet? [y/N] (default: no) ')
        except KeyboardInterrupt:
            exit()
        if tmp_fetchUserNames == 'y' or tmp_fetchUserNames == 'Y':
            fetch_user_names = True
        else:
            fetch_user_names = False
    
    if fetch_user_names == False:
        return None

    if userID in userNamesCache:
        return userNamesCache[userID]
    
    username = None
    
    print(f'Fetching username of {userID} from the internet...', file=sys.stderr, end="\r")
    try:
        with urllib.request.urlopen(f'https://steamcommunity.com/profiles/{userID}/') as response:
            html = response.read()
            html = html.decode('utf-8')
            a = html.find('<span class="actual_persona_name">') + 34
            b = html.find('</span>', a)
            username = html[a:b]
    except KeyboardInterrupt:
        print('', file=sys.stderr)
        print('Aborted', file=sys.stderr)
        tmp_cont = input('Continue running? [Y/n] (default: y): ')
        if len(tmp_cont) > 0 and (tmp_cont[0] == 'n' or tmp_cont[0] == 'N'):
            exit()
    if username != None:
        userNamesCache[userID] = username
    return username