# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['concise_concepts',
 'concise_concepts.conceptualizer',
 'concise_concepts.examples']

package_data = \
{'': ['*']}

install_requires = \
['gensim>=4,<5', 'spacy>=3,<4']

setup_kwargs = {
    'name': 'concise-concepts',
    'version': '0.2.3',
    'description': 'This repository contains an easy and intuitive approach to few-shot NER using most similar expansion over spaCy embeddings.',
    'long_description': '# Concise Concepts\nWhen wanting to apply NER to concise concepts, it is really easy to come up with examples, but pretty difficult to train an entire pipeline. Concise Concepts uses few-shot NER based on word embedding similarity to get you going with easy!\n\n# Install\n\n```\npip install concise-concepts\n```\n\n# Quickstart\n\n```python\nimport spacy\nfrom spacy import displacy\nimport concise_concepts\n\ndata = {\n    "fruit": ["apple", "pear", "orange"],\n    "vegetable": ["broccoli", "spinach", "tomato"],\n    "meat": ["beef", "pork", "fish", "lamb"]\n}\n\ntext = """\n    Heat the oil in a large pan and add the Onion, celery and carrots. \n    Then, cook over a medium–low heat for 10 minutes, or until softened. \n    Add the courgette, garlic, red peppers and oregano and cook for 2–3 minutes.\n    Later, add some oranges and chickens. """\n\nnlp = spacy.load("en_core_web_lg")\nnlp.add_pipe("concise_concepts", config={"data": data})\ndoc = nlp(text)\n\n\noptions = {"colors": {"fruit": "darkorange", "vegetable": "limegreen", "meat": "salmon"},\n           "ents": ["fruit", "vegetable", "meat"]}\n\ndisplacy.render(doc, style="ent", options=options)\n```\n![example](./img/example.png)\n## use specific number of words to expand over\n\n```python\ndata = {\n    "fruit": ["apple", "pear", "orange"],\n    "vegetable": ["broccoli", "spinach", "tomato"],\n    "meat": ["beef", "pork", "fish", "lamb"]\n}\n\ntopn = [50, 50, 150]\n\nassert len(topn) == len\n\nnlp.add_pipe("concise_concepts", config={"data": data, "topn": topn})\n````\n\n\n',
    'author': 'David Berenstein',
    'author_email': 'david.m.berenstein@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pandora-intelligence/concise-concepts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
