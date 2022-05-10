from src.google_trans_new import google_translator


class Translate:

    @staticmethod
    def translation(text: str, to_lang: str):
        if to_lang == 'en':
            return text
        translator = google_translator()
        translate_text = translator.translate(text, lang_src='en', lang_tgt=to_lang)
        return translate_text

    @staticmethod
    def translate_syntax(to_lang):
        syntax = Translate.translation("syntax", to_lang).lower()
        example = Translate.translation("for example", to_lang).lower()
        description = Translate.translation("description", to_lang).lower()

        helper = {
            "/start or /restart": {
                syntax: "/start",
                example: "/start",
                description: Translate.translation("Bot welcomes you and introduces itself.", to_lang)
            },
            "/tracks": {
                syntax: "/tracks " + Translate.translation(" singer_name", to_lang),
                example: "/tracks justin bieber",
                description: Translate.translation("Shows you top tracks of a given artist.", to_lang)
            },
            "/charts": {
                syntax: "/charts " + Translate.translation(" country_code", to_lang),
                example: "/charts ru",
                description: Translate.translation("""Shows you top tracks of a given country.\
            Statics of some countries are not displayed in it, so by default\
            it shows the top tracks of the USA.""", to_lang)
            },
            "/chart_artists": {
                syntax: "/char_artists " + "_".join(
                    Translate.translation("country code", to_lang)),
                example: "/char_artists ru",
                description: Translate.translation("""The same as the description of /charts command.\
                But instead of top tracks it shows most famous singers in the region.
                """, to_lang)
            },
            "/lyrics": {
                syntax: "/lyrics " + "_".join(Translate.translation("music name", to_lang)),
                example: "/lyrics genesis",
                description: Translate.translation("Shows the music lyrics.", to_lang)
            }
        }
        return helper
    @staticmethod
    def common_words(to_lang):
        album = Translate.translation("Album", to_lang)
        author = Translate.translation("Author", to_lang)