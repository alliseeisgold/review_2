from src.google_trans_new import google_translator


class Translate:

    @staticmethod
    def translation(text: str, to_lang: str):
        translator = google_translator()
        translate_text = translator.translate(text, lang_src='en', lang_tgt=to_lang)
        return translate_text
