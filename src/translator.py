from src.google_trans_new import google_translator


class Translate:

    @staticmethod
    def from_lang_to_lang(text: str, from_lang: str, to_lang: str):
        translator = google_translator()
        translate_text = translator.translate(text, lang_src=from_lang, lang_tgt=to_lang)
        return translate_text
