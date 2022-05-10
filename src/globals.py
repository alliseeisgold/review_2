class Globals:
    def __init__(self):
        self.lang = 'en'

    def chang_lang(self, new_lan: str):
        self.lang = new_lan

    def get_lang(self):
        return self.lang
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
    COMMON_WORDS = {
        "Album": "Album",
        "Tracks": "Track",
        "Author": "Author",
        "tracks_words": "Here's list of popular tracks of ",
        "charts_words": "Here's top chart of",
        "chart_artists_words": "Here's artists' top chart of",
        "lyrics_words": "Which song are you searching for?",
        "no_tracks": " hasn't any tracks."
    }