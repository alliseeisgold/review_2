import os

with open('./.env', 'r') as environment_variables:
    for line in environment_variables.readlines():
        key, value = line.split(' = ')
        os.environ[key] = value.strip()
BOT_TOKEN = os.environ["BOT_TOKEN"]
MUSIXMATCH_API_KEY = os.environ["MUSIXMATCH_API_KEY"]
