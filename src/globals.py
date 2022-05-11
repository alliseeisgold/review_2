from src.translator import Translate


class Globals:

    LANG = 'en'
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
    LOVED_STICKER = 'CAACAgIAAxkBAAEEtPBifA3NLVAdoXtH3LuqJrR5w9i_UAACbQAD29t-AAF1HuyF8vtEpSQE'
    COMMON_WORDS = {
        "Album": "Album",
        "Track": "Tracks",
        "Author": "Author",
        "Artist": "Singer",
        "tracks_words": "Here's list of popular tracks of ",
        "charts_words": "Here's top chart of",
        "chart_artists_words": "Here's artists' top chart of ",
        "lyrics_words": "Which song are you searching for?",
        "no_tracks": " hasn't any tracks."
    }
    HELPER = Translate.translate_syntax('en', 'en')
    LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'he': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'or': 'odia',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'tt': 'tatar',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'tk': 'turkmen',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'ug': 'uyghur',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
    }
