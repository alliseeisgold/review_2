import os

with open('.env', 'r') as environment_variables:
    for line in environment_variables.readlines():
        key, value = line.split(' = ')
        os.environ[key] = value.strip()
# BOT_TOKEN = os.environ["BOT_TOKEN"]
# MUSIXMATCH_API_KEY = os.environ["MUSIXMATCH_API_KEY"]
BOT_TOKEN = "5310805270:AAGgZ_v25a7jRfAzy0Di8AumP_UfG3v6ldg"
MUSIXMATCH_API_KEY = "352f922227a47654a366d2edc58fc7ae"