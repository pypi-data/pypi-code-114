import json
import os

from eurlex2lexparency.celex_manager import CelexBase
from eurlex2lexparency.extraction.meta_data.handler import default, Anchor
from eurlex2lexparency.extraction.meta_data.treaties import TreatyMetaData, cached_retrieve
from eurlex2lexparency.extraction.meta_data.cdm_data import TitlesRetriever, ActMetaData
from settings import LEXPATH


def dummy_1():
    from eurlex2lexparency.extraction.meta_data.title_parsing import TitleParser
    tp = TitleParser('ES')
    print(tp("Propuesta de REGLAMENTO DEL PARLAMENTO EUROPEO Y DEL CONSEJO POR EL QUE SE ESTABLECEN NORMAS ARMONIZADAS EN MATERIA DE INTELIGENCIA ARTIFICIAL (LEY DE INTELIGENCIA ARTIFICIAL) Y SE MODIFICAN DETERMINADOS ACTOS LEGISLATIVOS DE LA UNIÓN"))


def dummy_2():
    from eurlex2lexparency.extraction.meta_data.cdm_data import ActMetaData
    celex = CelexBase.from_string('32013R0575')
    lang = 'ES'
    print(json.dumps(ActMetaData.cached_retrieve(
        str(celex), lang,
        os.path.join(LEXPATH, celex.path, lang, 'head.json')).to_dict(),
                     default=default, ensure_ascii=False, indent=2))


def dummy_3():
    import os
    from lxml import etree as et
    from eurlex2lexparency.extraction.meta_data.cdm_data import ActMetaData
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'metas_1.html')
    d = et.ElementTree(file=data_path, parser=et.HTMLParser()).getroot()
    ActMetaData.parse(d)


def dummy_4():
    print(TitlesRetriever(
        'DE',
        ('http://publications.europa.eu/resource/celex/32009F0316',))
          .get_anchors())


def dummy_5():
    print(repr(TreatyMetaData.retrieve('http://publications.europa.eu/resource/authority/treaty/EEA', 'EN')))


def dummy_6():
    with open(r'C:\Users\Martin\lexparency\kernel\inte_data\3\2016\R\0679\DE\head.json', encoding='utf-8') as f:
        amd = ActMetaData.from_dict(json.load(f))
    print(amd.dumps())


def dummy_7():
    return Anchor.create("32017R0180", "Delegierte Verordnung (EU) 2017/180 der Kommission vom 24. Oktober 2016 <p class=\"lxp-title_essence\">Zur Ergänzung der Richtlinie 2013/36/EU des Europäischen Parlaments und des Rates durch technische Regulierungsstandards zur Festlegung der Normen für die Referenzportfoliobewertung und der Verfahren für die gemeinsame Nutzung der Bewertungen (Text von Bedeutung für den EWR. )</p>", 'DE')


def dummy_8():
    print(list(map(lambda x: str(x[0]), ActMetaData.kraken(
        f'act_is_about_lang', celex='32020R0653',
        language='de', lang3='deu'))))


def dummy_9():
    import json
    tmd = cached_retrieve('CHAR', 'ES')
    print(json.dumps(tmd.to_dict(), indent=2))


if __name__ == '__main__':
    dummy_1()
