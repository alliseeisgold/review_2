import telebot
from telebot import types
from src.config import *
from src.musixmatch import Musixmatch
from iso3166 import countries
from src.translator import Translate as trl
from src.constant import LANGUAGES
from src.lyrics import *
from src.globals import Globals

bot = telebot.TeleBot(BOT_TOKEN)

gll = Globals()


@bot.message_handler(commands=["start", "restart"])
def bot_start(message):
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


@bot.message_handler(commands=["set_lang"])
def set_lang(message):
    a = " ".join(
        [t for t in message.json["text"].split(" ")[1:]]
    ).strip()
    if not LANGUAGES.__contains__(a):
        error = """
        Invalid language code.\
        Please check [ISO639](https://ru.wikipedia.org/wiki/ISO_639) standard.
        """
        bot.send_message(message.chat.id,
                         text=trl.translation(error, gll.get_lang()),
                         parse_mode="Markdown")
        bot.send_sticker(message.chat.id,
                         Globals.WISE_STICKER)
    else:
        gll.chang_lang(a)
        m = "Successfully changed to *{}*".format(LANGUAGES[gll.get_lang()])
        bot.send_message(message.chat.id,
                         text=trl.translation(m, gll.get_lang()),
                         parse_mode="Markdown")
        bot.send_sticker(message.chat.id,
                         Globals.NICE_STICKER)
        for items in Globals.COMMON_WORDS:
            Globals.COMMON_WORDS[items] = trl.translation(
                Globals.COMMON_WORDS[items],
                gll.get_lang()
            )


@bot.message_handler(commands=["help"])
def help(message):
    ans = ""
    helper = trl.translate_syntax(gll.get_lang())
    for items in helper:
        ans += "<b><i>" + items + "</i></b>" + "\n"
        for item in helper[items]:
            ans += "<b>" + item + "</b>" + ": "
            for els in helper[items][item]:
                ans += els
            ans += '\n'
        ans += '\n'
    bot.send_message(message.chat.id,
                     text=ans,
                     parse_mode="HTML")


@bot.message_handler(commands=["tracks"])
def tracks_of_author(message):
    author = " ".join(
        [t.capitalize() for t in message.json["text"].split(" ")[1:]]
    ).strip()
    response, status_code = Musixmatch.get_tracks_of_author(author)
    if status_code == 200:
        ans = Globals.COMMON_WORDS["tracks_words"] + "*" + author + "*:\n"
        l = len(ans)
        for track in response["message"]["body"]["track_list"]:
            tr = track["track"]["track_name"]
            album_name = track["track"]["album_name"]
            url = track["track"]["track_share_url"]
            ans += Globals.COMMON_WORDS["Track"] + ": [{}]({})\n".format(tr, url)
            if album_name:
                ans += Globals.COMMON_WORDS["Album"] + ": *" + album_name + "*"
            ans += "\n\n"
        flag = False
        if l == len(ans):
            ans += Globals.COMMON_WORDS["Author"] + " *" + author + "*" + Globals.COMMON_WORDS["no_tracks"]
            flag = True
        bot.send_message(message.chat.id,
                         ans,
                         parse_mode="Markdown")
        if not flag:
            bot.send_sticker(message.chat.id, Globals.PLAYER_STICKER)
        else:
            bot.send_sticker(message.chat.id, Globals.JOKE_STICKER)
    else:
        bot.send_message(message.chat.id, text=Globals.MUSIXMATCH_ERROR)
        bot.send_sticker(message.chat.id, Globals.UPS_STICKER)


@bot.message_handler(commands=["charts"])
def get_charts_of_country(message):
    country_code = " ".join(message.json["text"].split(" ")[1:]).strip()
    if not country_code or len(country_code) == 0:
        bot.send_message(
            message.chat.id,
            text=Globals.FORMAT_ISO3166_ERROR,
        )
        bot.send_sticker(message.chat.id, Globals.UPS_STICKER)
        return
    else:
        response, status = Musixmatch.get_country_charts(country_code)
        if status == 200:
            try:
                cc = countries.get(country_code.lower()).name
            except:
                bot.send_message(
                    message.chat.id,
                    text=Globals.FORMAT_ISO3166_ERROR,
                )
                bot.send_sticker(message.chat.id, Globals.UPS_STICKER)
                return
            ans = Globals.COMMON_WORDS["charts_words"] + "*" + cc + "*:\n"
            for track in response["message"]["body"]["track_list"]:
                tr = track["track"]["track_name"]
                artist = track["track"]["artist_name"]
                url = track["track"]["track_share_url"]
                ans += Globals.COMMON_WORDS["Track"] + ": [{}]({})".format(tr, url) + "(lyrics)\n" + \
                       Globals.COMMON_WORDS["Artist"] + ": *" + artist + "*\n\n"
            bot.send_message(message.chat.id,
                             text=trl.translation(ans, to_lang=gll.get_lang()),
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


@bot.message_handler(commands=["chart_artists"])
def get_artists_of_country_chart(message):
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
                                 text=trl.translation("Didn't find country. ", gll.get_lang()) + \
                                      Globals.FORMAT_ISO3166_ERROR,
                                 parse_mode="Markdown")
                return
            country = countries.get(country_code.lower()).name
            answer = (
                    Globals.COMMON_WORDS["chart_artists_words"] + " *"
                    + country
                    + "*:\n"
            )
            answer = trl.translation(answer, gll.get_lang())
            for artist in response["message"]["body"]["artist_list"]:
                name = artist["artist"]["artist_name"]
                if len(artist["artist"]["artist_name_translation_list"]) > 0:
                    for transl in artist["artist"]["artist_name_translation_list"]:
                        if transl["artist_name_translation"]["language"] == "EN":
                            name = transl["artist_name_translation"]["translation"]
                            break
                answer += Globals.COMMON_WORDS["Artist"] + " *{}*\n\n".format(name)
            bot.send_message(message.chat.id,
                             text=trl.translation(answer, to_lang=gll.get_lang()),
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


@bot.message_handler(commands=["lyrics"])
def get_lyrics(message):
    res = [
        tmp.strip() for tmp in " ".join(
            message.json["text"].split(" ")[1:]
        ).split("-")
    ]
    if len(res) == 1 and not len(res[0]):
        bot.send_message(
            message.chat.id,
            text="Please add searching parameters: artist name "
                 "or/and track name.",
        )
        return
    elif len(res) == 1:
        track = res[0]
        artist = ""
    else:
        track, artist = res
    songs, status = search(track + " " + artist)
    if not status and "Error" in songs:
        bot.reply_to(message, text=songs["Error"])
        return
    elif not status:
        bot.reply_to(
            message,
            text=Globals.MUSIXMATCH_ERROR,
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
        callback.message.message_id
    )


def start_bot():
    bot.polling(none_stop=True, timeout=5)
