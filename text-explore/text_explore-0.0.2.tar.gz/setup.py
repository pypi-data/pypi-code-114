# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['text_explore']

package_data = \
{'': ['*']}

install_requires = \
['nltk==3.6.6']

setup_kwargs = {
    'name': 'text-explore',
    'version': '0.0.2',
    'description': 'A Python Package to perform Exploratory Data Analysis on Text Data.',
    'long_description': '# Text_Explore\n\nA Python Library to perform Exploratory Data Analysis on Text\n\nInstall Package\n\n```bash\npip install text_explore\n```\n\n## Using Package\n\n1. Access from class\n\n    ```python\n    # Access from a single class\n    from text_explore import TextExplore\n\n\n    text = """US actor Jussie Smollett has been sentenced to 150 days in jail after a jury found he lied to police about being the victim of a hate crime.\n\n    The former Empire star, 39, was found guilty in December of five charges of felony disorderly conduct after making false reports about the hoax attack.\n\n    The sentence also includes 30 months of probation and $145,000 (£110,000) in restitution and fines.\n\n    Following the sentence, Smollett said: "I did not do this!"\n\n    The trial stemmed from an incident three years ago when Smollett said he was attacked by two assailants.\n\n    The actor, who is black and gay, said the attackers shouted slurs at him and a Trump slogan, dumped a "chemical substance" on him and tied a noose around his neck while he was walking late at night in January 2019."""\n\n    doc = TextExplore(text)\n\n    # Count Number of Words in Text\n    print("Word Count:", doc.count_words())\n\n    # Count Number of Characters in Text\n    print("Characters Count:", doc.count_chars())\n\n    # Count Number of Stopwords in Text\n    print("Stopwords Count", doc.count_stopwords())\n\n    # Count Number of Syllables in Text\n    print("Syllables Count:", doc.count_syllables())\n\n    # Count Number of Sentences in Text\n    print("Sentences Count:", doc.count_sentences())\n\n    # Flesch reading ease score\n    print("Flesch reading ease:", doc.flesch_reading_ease())\n\n    # Flesch kincaid grade score\n    print("Flesch kincaid grade:", doc.flesch_kincaid_grade())\n    ```\n\n2. Access individual functions\n\n    ```python\n    # Access individual functions\n    from text_explore.counts import (\n        count_words,\n        count_chars,\n        count_stopwords,\n        count_syllables,\n        count_sentences,\n    )\n    from text_explore.readability import (\n        flesch_kincaid_grade, \n        flesch_reading_ease\n    )\n\n    # Count Number of Words in Text\n    print("Word Count:", count_words(text))\n\n    # Count Number of Characters in Text\n    print("Characters Count:", count_chars(text))\n\n    # Count Number of Stopwords in Text\n    print("Stopwords Count", count_stopwords(text))\n\n    # Count Number of Syllables in Text\n    print("Syllables Count:", count_syllables(text))\n\n    # Count Number of Sentences in Text\n    print("Sentences Count:", count_sentences(text))\n\n    # Flesch reading ease score\n    print("Flesch reading ease:", flesch_reading_ease(text))\n\n    # Flesch kincaid grade score\n    print("Flesch kincaid grade:", flesch_kincaid_grade(text))\n    ```\n',
    'author': 'Temiloluwa Awoyele',
    'author_email': 'awoyeletemiloluwa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/temmyzeus/text_explore',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
