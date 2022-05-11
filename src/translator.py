from googletrans import Translator


class Translate:

    @staticmethod
    def translation(text: str, dest: str, src: str):
        if src == dest:
            return text
        translator = Translator()
        translate_text = translator.translate(text, dest, src)
        return translate_text.text

    @staticmethod
    def translate_syntax(dest: str, src='en'):
        syntax = Translate.translation("syntax", dest, src).lower()
        example = Translate.translation("for example", dest, src).lower()
        description = Translate.translation("description", dest, src).lower()
        helper = {
            "/start or /restart": {
                syntax: "/start",
                example: "/start",
                description: Translate.translation("Bot welcomes you and introduces itself.",
                                                   dest, src)
            },
            "/tracks": {
                syntax: "/tracks " + Translate.translation(" singer_name", dest, src),
                example: "/tracks justin bieber",
                description: Translate.translation("Shows you top tracks of a given artist.",
                                                   dest, src)
            },
            "/charts": {
                syntax: "/charts " + Translate.translation(" country_code",
                                                           dest, src),
                example: "/charts ru",
                description: Translate.translation(
                    "Shows you top tracks of a given country. "
                    "Statics of some countries are not displayed in it, "
                    "so by default it shows the top tracks of the USA.",
                    dest, src)
            },
            "/chart_artists": {
                syntax: "/char_artists " + Translate.translation("country code",
                                                                 dest, src),
                example: "/char_artists ru",
                description: Translate.translation(
                    "The same as the description of /charts command. But instead of "
                    "top tracks it shows most famous singers in the region.",
                    dest, src)
            },
            "/lyrics": {
                syntax: "/lyrics " + Translate.translation("music_name", dest, src),
                example: "/lyrics genesis",
                description: Translate.translation("Shows the music lyrics.", dest, src)
            }
        }
        return helper
