import sys
from jinja2 import Template, Environment, FileSystemLoader

import utils, getopt
import useraccounts, localconfig, friends, games, cachedimages, achievements, timeplayed

def printHelp():
    print(f'Usage:\n\tpython {sys.argv[0]} [options]')
    print(f'Options:')
    print('\t{:20}\t{}'.format('-h, --help', 'show help'))
    print('\t{:20}\t{}'.format('-y', 'answer yes to all questions (except ones about paths)'))
    print('\t{:20}\t{}'.format('-d, --default-path', 'do not ask for paths, use defaults instead'))

def parseArgv():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'hyd', ['help', 'default-path'])
    except getopt.GetoptError as err:
        print(err)
        printHelp()
        return 1, []

    if 'help' in args:
        printHelp()
        return 1
    for o, a in optlist:
        if o == '-h' or o == '--help':
            printHelp()
            return 1
        elif o == '-y':
            utils.fetch_game_names = True
            utils.fetch_user_names = True
            cachedimages.export_dir = ''
        elif o == '-d' or o == '--default-path':
            utils.use_default_install = 'y'
            utils.use_default_appdata = 'y'
    return 0

errcode = parseArgv()
if errcode != 0:
    exit(errcode)


#Ask, so user won't be asked later
utils.getInstallPath()
utils.getAppdataPath()


useraccounts_data = useraccounts.run()
useraccounts_data = useraccounts_data['users']
localconfig_data = localconfig.run()
friends_data = friends.run()
games_data = games.run()
cachedimages_data = cachedimages.run()
achievements_data = achievements.run()
timeplayed_data = timeplayed.run()

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('temp.html')
output_from_parsed_template = template.render(
    useraccounts=useraccounts_data,
    localconfig=localconfig_data,
    friends=friends_data,
    games=games_data,
    cachedimages=cachedimages_data,
    achievements=achievements_data,
    timeplayed=timeplayed_data
)

with open("index.html", "w") as fh:
    fh.write(output_from_parsed_template)

print("Done.")
