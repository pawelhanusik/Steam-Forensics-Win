# Steam Forensics for Windows

Tool to help digital forensics of Steam app on Windows

### Data it gets

- user accounts - logged in user's accounts
- local config - default audio devices' names
- friends - user's friends
- games - user's games
- achievements - user's achievements
- time played - shows how much time user's friends were playing some games
- cached images - images cached while browsing for eg. steam store

### How to

Make sure you have python3 installed.

Install dependencies:  
`pip install -r requirements.txt`

Run:  
`python main.py`

### Options

-h, --help - show help  
-y - answer `yes` to all questions (except ones about paths)  
-d, --default-path - do not ask for paths, use defaults instead
