from spacy.language import Language
from .language_data import STOP_WORDS


class Hebrew(Language):
    lang = 'he'

    class Defaults(Language.Defaults):
        lex_attr_getters = dict(Language.Defaults.lex_attr_getters)

        stop_words = STOP_WORDS
