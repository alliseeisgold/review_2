from translate import Translator


class Translate:

    @staticmethod
    def from_lang_to_lang(text: str, from_lang: str, to_lang: str):
        t = Translator(from_lang=from_lang, to_lang=to_lang)
        return t.translate(text)
