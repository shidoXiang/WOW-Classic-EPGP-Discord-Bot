## How to run:

First copy settings.py to local_settings.json and fill in admin_token and discord_token. 

Run this cmd for install dependency and run:
```bash
$ source buildstart.sh
```
If there is any error in pip3 install, try updating pip3 first.

If there is no dependency update, just run:
```bash
$ source start.sh
```

To install new library:
Make sure these commands need to be done while in venv:
```bash
$ pip3 install libraryName
$ pip3 freeze > requirements.txt
```

To deactivate the virtual env:
```bash
$ deactivate
```
