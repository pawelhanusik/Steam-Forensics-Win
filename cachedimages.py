import os, shutil, filetype
import base64

import utils

export_dir = None

def run():
    global export_dir

    cachedir = utils.getAppdataPath() + '/htmlcache/Cache/'
    files = os.listdir(cachedir)
    
    if export_dir == None:
        try:
            export_dir = input("Please specify images export dir name (leave empty to embed images into html): ")
        except KeyboardInterrupt:
            exit()
    if len(export_dir) > 0:
        if os.path.exists(export_dir):
            try:
                deleteOrNot = input("Export dir already exists. Delete its contents? [y/N] (default: no) ")
            except KeyboardInterrupt:
                exit()
            if len(deleteOrNot) > 0 and (deleteOrNot[0] == 'y' or deleteOrNot[0] == 'Y'):
                shutil.rmtree(export_dir)
                os.mkdir(export_dir)
        else:
            os.mkdir(export_dir)
    
    images = []
    for file in files:
        filepath = cachedir + file
        kind = filetype.guess(filepath)
        if kind == None:
            continue
        if kind.mime.split('/')[0] == 'image':
            if len(export_dir) > 0:
                full_path = export_dir + '/' + file + '.' + kind.mime.split('/')[1]
                images += [full_path]
                shutil.copyfile(filepath, full_path)
            else:
                file = open(filepath, 'rb')
                contents = file.read()
                images += ['data:' + kind.mime + ';base64, ' + base64.b64encode(contents).decode('ascii')]
    return images
