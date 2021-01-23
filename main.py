import sys
from jinja2 import Template, Environment, FileSystemLoader

import utils
import useraccounts, localconfig, friends, games, cachedimages, achievements, timeplayed

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
