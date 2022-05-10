import telebot
from src.config import *
from src.musixmatch import Musixmatch
from iso3166 import countries
from src.translator import Translate

bot = telebot.TeleBot(BOT_TOKEN)

lang = "en"


@bot.message_handler(commands=["start"])
def set_lang(message):
    user = message.from_user.first_name
    greeting = """
                Hello, {}! Do you know who I am? ...
                Yes! I'm bot. I help you to find lyrics of 
                a given music, top singers of the country you gave,
                top tracks of your favourite singer and others or the most
                popular artists in the country you want.
                ----------------------------------------------------------
                Привет, {}! Ты знаешь, кто я такой? ...
                Да! Я бот. Я помогу тебе найти тексты
                данной музыки, лучших исполнителей страны, которую вы указали,
                лучшие треки вашего любимого певца и другие или самые
                популярные артисты в нужной вам стране.
        """.format(user, user)
    bot.send_message(message.chat.id, text=greeting)


@bot.message_handler(commands=["set_lang"])
def set_lang(message):
    global lang
    lang = " ".join(
        [t for t in message.json["text"].split(" ")[1:]]
    ).strip()


@bot.message_handler(commands=["help"])
def help(message):
    m = "/tracks <singer name>, for example: /tracks justin bieber "
    ans = m + "\n" + "/charts <country_code>. for example: /charts ru"
    bot.send_message(message.chat.id, text=Translate.translation(ans, to_lang=lang))


@bot.message_handler(commands=["tracks"])
def tracks_of_author(message):
    author = " ".join(
        [t.capitalize() for t in message.json["text"].split(" ")[1:]]
    ).strip()
    response, status = Musixmatch.get_tracks_of_author(author)
    if status == 200:
        ans = "Here's list of popular tracks of *" + author + "*:\n"
        l = len(ans)
        for track in response["message"]["body"]["track_list"]:
            tr = track["track"]["track_name"]
            album_name = track["track"]["album_name"]
            url = track["track"]["track_share_url"]
            ans += f"Track: [{tr}]({url})\n"
            if album_name:
                ans += "Album: *" + album_name + "*"
            ans += "\n\n"
        if l == len(ans):
            ans += "Author " + author + " hasn't any tracks."
        bot.send_message(message.chat.id, text=Translate.translation(ans, to_lang=lang), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, text=MUSIXMATCH_ERROR)


@bot.message_handler(commands=["charts"])
def get_charts_of_country(message):
    country_code = " ".join(message.json["text"].split(" ")[1:]).strip()
    if not country_code or len(country_code) == 0:
        bot.send_message(
            message.chat.id,
            text=FORMAT_ISO3166_ERROR,
        )
        return
    else:
        response, status = Musixmatch.get_country_charts(country_code)
    if status == 200:
        try:
            cc = countries.get(country_code.lower()).name
        except:
            bot.send_message(
                message.chat.id,
                text=FORMAT_ISO3166_ERROR,
            )
            return
        answer = "Here's top chart of *" + cc + "*:\n"
        for track in response["message"]["body"]["track_list"]:
            tr = track["track"]["track_name"]
            artist = track["track"]["artist_name"]
            url = track["track"]["track_share_url"]
            answer += f"Track: [{tr}]({url}) (lyrics)\nArtist: *" + artist \
                      + "*\n\n"
        bot.send_message(message.chat.id, text=Translate.translation(answer, to_lang=lang), parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, text=MUSIXMATCH_ERROR)


@bot.message_handler(commands=["chart_artists"])
def get_artists_of_country_chart(message):
    country_code = " ".join(message.json["text"].split(" ")[1:]).strip()
    if not country_code or len(country_code) == 0:
        bot.send_message(
            message.chat.id,
            text=FORMAT_ISO3166_ERROR,
        )
        return

    response, status = Musixmatch.get_chart_artists(country_code)

    if status == 200:
        if not countries.__contains__(country_code.lower()):
            bot.send_message(message.chat.id, text="Didn't find country. " + FORMAT_ISO3166_ERROR,
                             parse_mode="Markdown")
            return
        country = countries.get(country_code.lower()).name
        answer = (
                "Here's artists' top chart of *"
                + country
                + "*:\n"
        )
        for artist in response["message"]["body"]["artist_list"]:
            name = artist["artist"]["artist_name"]
            if len(artist["artist"]["artist_name_translation_list"]) > 0:
                for transl in artist["artist"]["artist_name_translation_list"]:
                    if transl["artist_name_translation"]["language"] == "EN":
                        name = transl["artist_name_translation"]["translation"]
                        break
            answer += f"Artist: *{name}*\n\n"
        bot.send_message(message.chat.id, text=Translate.translation(answer, to_lang=lang), parse_mode="Markdown")
        return
    bot.send_message(
        message.chat.id,
        text=MUSIXMATCH_ERROR,
    )


if __name__ == '__main__':
    MUSIXMATCH_ERROR = """Couldn't connect to MusixMatch. Please try again.
                           Anyway you can report it to me @alliseeisgoal. 
                           Thanks! """
    FORMAT_ISO3166_ERROR = "Please pass country code in the format of ISO3166. For example: /charts ru"
    bot.polling(none_stop=True, timeout=5)
