from config import X_RAPIDAPI_HOST
from config import X_RAPIDAPI_KEY
from googletrans import Translator

def detect_language(s: str) -> str:
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
    data = {'q': s}
    heders = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": X_RAPIDAPI_KEY,
        "X-RapidAPI-Host": X_RAPIDAPI_HOST
    }
return s


def detect_language(text):
        translator = Translator()
        lang = translator.detect(text)
        return lang.lang

    # TODO: из JSON выданного в ответ на запрос извлечь язык
 #TODO: вернуть язык из функции
    # phind в помощь

#TODO: созать функцию перевода строки (первый параметр функции)
# с языка from_lang на язык to_lang (2 параметра функции)

#TODO: создать функцию возвращающую список язвков


# a = detect_language("""Vova Eremenko""")
# b = detect_language("Dmitriy Shutov")
# print(a, b)

if __name__ == '__main__':