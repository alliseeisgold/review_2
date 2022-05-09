import telebot
from src.config import *
from src.musixmatch import Musixmatch
from iso3166 import countries

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["help"])
def help(message):
    helper = """/tracks <singer name>, for example: /tracks justin bieber \n
             /charts <country_code in iso3166 standard>. for example: /charts ru
            """
    bot.send_message(message.chat.id, text=helper, parse_mode="Markdown")


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
        bot.send_message(message.chat.id, text=ans, parse_mode="Markdown")
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
        bot.send_message(message.chat.id, text=answer, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, text=MUSIXMATCH_ERROR)


if __name__ == '__main__':
    MUSIXMATCH_ERROR = """Couldn't connect to MusixMatch. Please try again.
                           Anyway you can report it to me @alliseeisgoal. 
                           Thanks! """
    FORMAT_ISO3166_ERROR = "Please pass country code in the format of ISO3166. For example: /charts ru"
    bot.polling(none_stop=True, timeout=5)
