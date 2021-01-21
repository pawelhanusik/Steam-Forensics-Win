import os

default_install_path = "C:/Program Files (x86)/Steam"
default_appdata_path = os.getenv('LOCALAPPDATA') + "/Steam/"

use_default_install = None
use_default_appdata = None

def getInstallPath():
    global use_default_install
    if use_default_install == None:
        use_default_install = input(f'Use default Steam install path? ({default_install_path}) [Y/n] (default: Y): ')
    if len(use_default_install) > 0 and ( use_default_install[0] == 'n' or use_default_install[0] == 'N' ):
        return input('Input Steam install path: ')
    return default_install_path

def getAppdataPath():
    global use_default_appdata
    if use_default_appdata == None:
        use_default_appdata = input(f'Use default Steam appdata path? ({default_appdata_path}) [Y/n] (default: Y): ')
    if len(use_default_appdata) > 0 and ( use_default_appdata[0] == 'n' or use_default_appdata[0] == 'N' ):
        return input('Input Steam appdata path: ')
    return default_appdata_path

