import os

# with open('./.env', 'r') as environment_variables:
#     for line in environment_variables.readlines():
#         key, value = line.split(' = ')
#         os.environ[key] = value.strip()
BOT_TOKEN = os.environ["BOT_TOKEN"]
MUSIXMATCH_API_KEY = os.environ["MUSIXMATCH_API_KEY"]
YA_TRANSLATOR_API = os.environ["TRANSLATOR_API_KEY"]
GREETING_STICKER = 'CAACAgIAAxkBAAEEsPRiehsgmOuXxcW_U0LPiYvB3_tP9QACbwAD29t-AAGZW1Coe5OAdCQE'
UPS_STICKER = 'CAACAgIAAxkBAAEEsPhiehuiemVkEPE34Pg14b2Gqb3oOgACYgAD29t-AAGOFzVmmxPyHCQE'
WISE_STICKER = 'CAACAgIAAxkBAAEEsP9iei0cSLmlGxWhTZOHT2XB92ofsgACOgAD29t-AAHzlAwLbxbUmiQE'
NICE_STICKER = 'CAACAgIAAxkBAAEEsQhiejp1hEOKUGEFI2bUcz1ZOufJbQACPwAD29t-AAH05pw4AeSqaSQE'
MUSIXMATCH_ERROR = """Couldn't connect to MusixMatch. Please try again.
                            Anyway you can report it to me @alliseeisgoal.
                            Thanks! """
FORMAT_ISO3166_ERROR = "Please pass country code in the format of ISO3166. For example: /charts ru"
PLAYER_STICKER = 'CAACAgIAAxkBAAEEsR1iekmK3SMjX34qYo5HAwsJEFagWAACZwAD29t-AAE93xTvYUeRnyQE'
JOKE_STICKER = 'CAACAgIAAxkBAAEEsTBiekzPhZNVM1m1idPDhYA2wZcC9AACaAAD29t-AAH9Ee05XbvckyQE'
ERROR_STICKER = 'CAACAgIAAxkBAAEEsTRiek3HOyR1_r--5a3U-oStqfMY7wACYwAD29t-AAGMnQU950KD5yQE'