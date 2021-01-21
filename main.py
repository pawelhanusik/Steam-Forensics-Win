import sys
from jinja2 import Template, Environment, FileSystemLoader

import useraccounts, localconfig, friends, games

modules = {
    'useraccounts': useraccounts.run,
    'localconfig': localconfig.run,
    'friends': friends.run,
    'games': games.run
}

useraccounts = useraccounts.run()
useraccounts = useraccounts['users']
localconfig = localconfig.run()
friends = friends.run()
games = games.run()

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('temp.html')
output_from_parsed_template = template.render(
    useraccounts=useraccounts,
    localconfig=localconfig,
    friends=friends,
    games=games
)

with open("index.html", "w") as fh:
    fh.write(output_from_parsed_template)
