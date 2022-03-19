import os

from eurlex2lexparency.extraction.full_bodies.formex import FormexLoader
from eurlex2lexparency.extraction.full_bodies.html import HTMLoader
from eurlex2lexparency.extraction.meta_data.language_format import EurLexLanguagesAndFormats
from settings import LEXPATH


def load_formex():
    fl = FormexLoader(
        os.path.join(LEXPATH, r'5\2021\PC\0206\DE\initial\fmx',),
        '52021PC0206', 'DE').document


def load_lang_fmt():
    return EurLexLanguagesAndFormats(
        os.path.join(LEXPATH, r'1\2016\E', 'RDF', 'initial'),
        '12016E'
    )


def load_html(source_url):
    return HTMLoader(
        os.path.join(
            LEXPATH, r'5\2021\PC\0206', 'DE', 'initial', 'htm'),
        source_url
    ).document


if __name__ == '__main__':
    # lf = load_lang_fmt()
    # print(lf)
    load_html('https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:52021PC0206')
    # load_formex()
