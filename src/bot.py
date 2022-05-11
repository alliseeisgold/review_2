import telebot
from telebot import types
from iso3166 import countries
from src.config import BOT_TOKEN
from src.globals import Globals
from src.lyrics import parse_lyrics, search
from src.musixmatch import Musixmatch
from src.translator import Translate as trl

bot = telebot.TeleBot(BOT_TOKEN)

# Initializing Globals: only lang

"""
    Commands /start and /restart has same functions: 
        1. welcomes the user 
        2. introduces itself
"""


@bot.message_handler(commands=["start", "restart"])
def bot_start(message):
    """
        Sends the greeting text to user.
        Sends welcome sticker. :)
    :param message:
    """
    user = message.from_user.first_name
    greeting = """
<b>[en]</b>\nHello,  <b>{}</b> ! Do you know who I am? ...\
Yes! I'm <b>music_render</b> bot. \
I help you to find lyrics of a given music, top singers of \
the country you gave, top tracks of your favourite singer \
and others or the most popular artists in the country you want.\n
------------------------------------------------------------------------\n
<b>[ru]</b>\nПривет, {}! Ты знаешь, кто я такой? ... \
Да! Я <b>music_render</b> бот. Я помогу тебе найти текст музыки, которой \
ты хочешь, лучших исполнителей страны, которую ты указал, лучшие треки \
твоего любимого певца и не только и самые популярные \
артисты в нужной тебе стране.
""".format(user, user)
    bot.send_message(
        message.chat.id,
        text=greeting,
        parse_mode="HTML"
    )
    bot.send_sticker(
        message.chat.id,
        Globals.GREETING_STICKER
    )


"""
    Command /set_lang sets a new lang. By default language is english
"""


@bot.message_handler(commands=["set_lang"])
def set_lang(message):
    """
        This function works like that:
            1. Parses the text(language_code) after this command and gets it.
            2. Checks if this language_code corresponds to the ISO639 format:
                a) if it is true: changes the language.
                b) if it is false: sends error message with pointing to read the ISO639 documentation.
            (And also doesn't forget about stickers ^_^)
    :param message:
    :return:
    """
    a = " ".join(
        [t for t in message.json["text"].split(" ")[1:]]
    ).strip()
    if not Globals.LANGUAGES.__contains__(a):
        error = "Invalid language code. " \
                "Please check [ISO639](https://ru.wikipedia.org/wiki/ISO_639) standard."
        bot.send_message(message.chat.id,
                         text=trl.translation(error, Globals.LANG, 'en'),
                         parse_mode="Markdown")
        bot.send_sticker(message.chat.id,
                         Globals.WISE_STICKER)
    else:
        if a == Globals.LANG:
            repeating = trl.translation(
                "Nigga are you kidding me? My language is the same.",
                a, 'en'
            )
            bot.send_message(message.chat.id,
                             text=repeating,
                             )
        else:
            m = trl.translation("Successfully changed to *{}*".format(
                Globals.LANGUAGES[a]),
                a, 'en')
            for items in Globals.COMMON_WORDS:
                Globals.COMMON_WORDS[items] = trl.translation(
                    Globals.COMMON_WORDS[items],
                    a,
                    Globals.LANG
                )
            Globals.HELPER = trl.translate_syntax(a)
            Globals.FORMAT_ISO3166_ERROR = trl.translation(
                Globals.FORMAT_ISO3166_ERROR,
                a,
                Globals.LANG
            )
            Globals.MUSIXMATCH_ERROR = trl.translation(
                Globals.MUSIXMATCH_ERROR,
                a,
                Globals.LANG
            )
            Globals.LANG = a
            bot.send_message(message.chat.id,
                             text=m,
                             parse_mode="Markdown"
                             )
            bot.send_sticker(message.chat.id,
                             Globals.NICE_STICKER)


"""
    Command /help shows information about bot commands: syntax, example and description. 
"""


@bot.message_handler(commands=["help"])
def help(message):
    """
        This function works like that:
            1. Gets from Globals variable HELPER(it is map).
            2. Creates variable ans from HELPER the (Keys(commands))
               values(Syntax: value, Example: value, Description: value)
            3. Sends to user value of ans with HTML parse_mode and also sticker.
    :param message:
    :return:
    """
    ans = ""
    helper = Globals.HELPER
    for items in helper:
        ans += "<b><i>" + items + "</i></b>" + "\n"
        for item in helper[items]:
            ans += "<b>" + item + "</b>" + ": "
            for els in helper[items][item]:
                ans += els
            ans += '\n\n'
        ans += '\n'
    bot.send_message(message.chat.id,
                     text=ans,
                     parse_mode="HTML")


"""
    Command /track shows top tracks of a given singer.
"""


@bot.message_handler(commands=["tracks"])
def tracks_of_author(message):
    """
        This function works like that:
            1. Parses the text (author ) after this command and gets it.
            2. Gets the values[response, status_code] of
               Musixmatch.get_tracks_of_author(author)
            3. If status_code:
                a) not equal to 200, (it means that request wasn't successful: look at documentation);
                   bot sends message with Globals.MUSIXMATCH_ERROR
                b) equal to 200, (it means the request was successful)
                   bot sends message with top tracks of a given author
                   or if this author hasn't tracks sends messages with that.
                   ( also sends stickers:) )
    :param message:
    :return:
    """
    author = " ".join(
        [t.capitalize() for t in message.json["text"].split(" ")[1:]]
    ).strip()
    response, status_code = Musixmatch.get_tracks_of_author(author)
    if status_code == 200:
        ans = Globals.COMMON_WORDS["tracks_words"] + " *" + author + "*:\n"
        l = len(ans)
        for track in response["message"]["body"]["track_list"]:
            tr = track["track"]["track_name"]
            album_name = track["track"]["album_name"]
            url = track["track"]["track_share_url"]
            if len(tr) < 30:
                ans += Globals.COMMON_WORDS["Track"] + ": [{}]({})\n".format(tr, url)
                if album_name:
                    ans += Globals.COMMON_WORDS["Album"] + ": *" + album_name + "*"
                ans += "\n\n"
        flag = False
        if l == len(ans):
            ans += Globals.COMMON_WORDS["Author"] + " *" + author + "*" + \
                   Globals.COMMON_WORDS["no_tracks"]
            flag = True
        bot.send_message(message.chat.id,
                         ans,
                         parse_mode="Markdown"
                         )
        if not flag:
            bot.send_sticker(message.chat.id, Globals.PLAYER_STICKER)
        else:
            bot.send_sticker(message.chat.id, Globals.JOKE_STICKER)
    else:
        bot.send_message(message.chat.id, text=Globals.MUSIXMATCH_ERROR)
        bot.send_sticker(message.chat.id, Globals.UPS_STICKER)


"""
    Command /charts shows top tracks in a given country with their authors.
    NOTE: as bot gets this information from musixmatch.com so may be some countries
          statistics not displayed there, that's why by default it gets US charts and shows
          it when this happens.
"""


@bot.message_handler(commands=["charts"])
def get_charts_of_country(message):
    """
        This function works like that:
            1. Parses the text (country_code) after this command and gets it.
            2. Checks if this country_code corresponds to the ISO639 format:
                a) if it is false:
                    sends the message with Globals.FORMAT_ISO3166_ERROR
                    and suggests to read about this format on wiki.
                b) if it is true:
                    gets values[response, status_code] from func.
                    Musixmatch.get_country_charts(country_code).
                    if status_code:
                        a') not equal to 200, (it means that request wasn't successful: look at documentation);
                        bot sends message with Globals.MUSIXMATCH_ERROR
                        b') equal to 200, (it means the request was successful)
                       bot sends message with top tracks of a given country
                       with their authors.
                       ( also sends stickers:) )
    :param message:
    :return:
    """
    country_code = " ".join(message.json["text"].split(" ")[1:]).strip()
    if not country_code or len(country_code) == 0:
        bot.send_message(
            message.chat.id,
            text=Globals.FORMAT_ISO3166_ERROR,
        )
        bot.send_sticker(message.chat.id, Globals.UPS_STICKER)
    else:
        response, status = Musixmatch.get_country_charts(country_code)
        if status == 200:
            try:
                cc = trl.translation(countries.get(country_code.lower()).name,
                                     Globals.LANG, 'en')
            except:
                bot.send_message(
                    message.chat.id,
                    text=Globals.FORMAT_ISO3166_ERROR,
                )
                bot.send_sticker(message.chat.id, Globals.UPS_STICKER)
                return
            ans = Globals.COMMON_WORDS["charts_words"] + " *" + cc + "*:\n"
            for track in response["message"]["body"]["track_list"]:
                tr = track["track"]["track_name"]
                artist = track["track"]["artist_name"]
                url = track["track"]["track_share_url"]
                ans += Globals.COMMON_WORDS["Track"] + ": [{}]({})".format(tr, url) + "(lyrics)\n" + \
                       Globals.COMMON_WORDS["Artist"] + ": *" + artist + "*\n\n"
            bot.send_message(message.chat.id,
                             ans,
                             parse_mode="Markdown")
            bot.send_sticker(message.chat.id, Globals.PLAYER_STICKER)
        else:
            bot.send_message(
                message.chat.id,
                text=Globals.MUSIXMATCH_ERROR)
            bot.send_sticker(
                message.chat.id,
                Globals.ERROR_STICKER
            )


"""
    Commands /chart_artists works as /charts command, but it shows only famous singers
    in the given country.  
    NOTE: the same notes as in /charts.
"""


@bot.message_handler(commands=["chart_artists"])
def get_artists_of_country_chart(message):
    """
        This function works like function get_charts_of_country,
        but it sends top singers only.
    :param message:
    :return:
    """
    country_code = " ".join(message.json["text"].split(" ")[1:]).strip()
    if not country_code or len(country_code) == 0:
        bot.send_message(
            message.chat.id,
            text=Globals.FORMAT_ISO3166_ERROR,
        )
        bot.send_sticker(message.chat.id, Globals.UPS_STICKER)
    else:
        response, status = Musixmatch.get_chart_artists(country_code)
        if status == 200:
            if not countries.__contains__(country_code.lower()):
                bot.send_message(message.chat.id,
                                 text=trl.translation("Didn't find country. ",
                                                      Globals.LANG,
                                                      'en') + Globals.FORMAT_ISO3166_ERROR,
                                 parse_mode="Markdown")
                return
            country = trl.translation(
                countries.get(country_code.lower()).name,
                Globals.LANG, 'en')
            answer = (
                    Globals.COMMON_WORDS["chart_artists_words"] + " *"
                    + country
                    + "*: \n\n"
            )
            for artist in response["message"]["body"]["artist_list"]:
                name = artist["artist"]["artist_name"]
                if len(artist["artist"]["artist_name_translation_list"]) > 0:
                    for transl in artist["artist"]["artist_name_translation_list"]:
                        if transl["artist_name_translation"]["language"] == "EN":
                            name = transl["artist_name_translation"]["translation"]
                            break
                answer += Globals.COMMON_WORDS["Artist"] + ": *{}*\n".format(name)
            bot.send_message(message.chat.id,
                             text=answer,
                             parse_mode="Markdown")
        else:
            bot.send_message(
                message.chat.id,
                text=Globals.MUSIXMATCH_ERROR,
            )
            bot.send_sticker(
                message.chat.id,
                Globals.ERROR_STICKER
            )


def short(name):
    """
        This function works like that:
            1. Gets argument name and split it to two parts by '-'
            2. The first part will be artist and the second track
            3. If artist length or track length more than 15 gets
               the first 15 chars.

    :param name: str
    :return [artist: str, track: str]: list
    """
    artist = ''
    track = ''
    if "-" in name:
        l = name.split("-")
        artist, track = l[0], " ".join(l[1:])
    elif " " in name:
        l = name.split(" ")
        artist, track = l[:-1], l[-1:]
    if len(artist) > 15:
        artist = artist[:15]
    if len(track) > 15:
        track = track[:15]
    return [artist, track]


"""
    Command /lyrics shows lyrics og a given music.
    NOTE: it may be that there are several tracks with the 
          same name, so you are invited to choose the one you wanted
"""


@bot.message_handler(commands=["lyrics"])
def get_lyrics(message):
    """
        This function works like that:
            1. Parses arguments of the command (artist or music_name or both of them) and gets it
            2. If arguments are incorrect it sends an error message.
            3. If arguments are correct it uses search() function from lyrics module.
            4. And if the search gives status_code 200 that means request was successful,
               it clarifies from you what song you had in mind.
            5. And if the search wasn't successful it sends y

    :param message:
    :return:
    """
    res = [
        tmp.strip() for tmp in " ".join(
            message.json["text"].split(" ")[1:]
        ).split("-")
    ]
    if len(res) == 1 and not len(res[0]):
        bot.send_message(
            message.chat.id,
            text=trl.translation(
                "Please add searching parameters: artist name "
                "or/and track name.",
                Globals.LANG, 'en'),
        )
        return
    elif len(res) == 1:
        track = res[0]
        artist = ""
    else:
        track, artist = res
    songs, status = search(track + " " + artist)
    if not status and "Error" in songs:
        bot.reply_to(message, text=trl.translation(songs["Error"], Globals.LANG, 'en'))
        bot.send_sticker(
            message.chat.id,
            Globals.UPS_STICKER)
        return
    elif not status:
        bot.reply_to(
            message,
            text=Globals.MUSIXMATCH_ERROR,
        )
        bot.send_sticker(
            message.chat.id,
            Globals.ERROR_STICKER
        )
        return
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for k in songs:
        shortened = short(k)
        button = types.InlineKeyboardButton(k,
                                            callback_data=" ".join(shortened)
                                            )
        keyboard.add(button)
    text = Globals.COMMON_WORDS["lyrics_words"] + "\n"
    bot.send_message(message.chat.id,
                     text=text,
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: True)
def callbacks(callback):
    m_kup = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Back", callback_data="B")
    m_kup.add(button)
    k = callback.data
    songs, status = search(k)
    for i in songs:
        if k in " ".join(short(i)):
            k = i
            break
    if status:
        text = parse_lyrics(songs[k])
    else:
        text = Globals.MUSIXMATCH_ERROR
    bot.edit_message_text(
        text[:4096],
        callback.message.chat.id,
        callback.message.message_id,
    )
    bot.send_sticker(callback.message.chat.id,
                     Globals.LOVED_STICKER)


def start_bot():
    bot.polling(none_stop=True, timeout=5)
