import sys
from jinja2 import Template, Environment, FileSystemLoader

import utils
import useraccounts, localconfig, friends, games, cachedimages, achievements, timeplayed

def printHelp():
    print(f'Usage:\n\tpython {sys.argv[0]} [options]')
    print(f'Options:')
    print('\t{:20}\t{}'.format('-h, --help', 'show help'))
    print('\t{:20}\t{}'.format('-y', 'answer yes to all questions (except ones about paths)'))
    print('\t{:20}\t{}'.format('-d, --default-path', 'do not ask for paths, use defaults instead'))

if '-h' in sys.argv or '--help' in sys.argv or 'help' in sys.argv:
    printHelp()
    exit()
if '-y' in sys.argv:
    utils.fetch_game_names = True
    utils.fetch_user_names = True
if '-d' in sys.argv or '--default-path' in sys.argv:
    utils.use_default_install = 'y'
    utils.use_default_appdata = 'y'


#Ask, so user won't be asked later
utils.getInstallPath()
utils.getAppdataPath()


useraccounts = useraccounts.run()
useraccounts = useraccounts['users']
localconfig = localconfig.run()
friends = friends.run()
games = games.run()
cachedimages = cachedimages.run()
achievements = achievements.run()
timeplayed = timeplayed.run()

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('temp.html')
output_from_parsed_template = template.render(
    useraccounts=useraccounts,
    localconfig=localconfig,
    friends=friends,
    games=games,
    cachedimages=cachedimages,
    achievements=achievements,
    timeplayed=timeplayed
)

with open("index.html", "w") as fh:
    fh.write(output_from_parsed_template)

print("Done.")
