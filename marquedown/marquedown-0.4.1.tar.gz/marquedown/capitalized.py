import re


RE_CAPITALIZED = re.compile(r'\<p\>(\s+(?!\\))\[(\w)\]')


def _repl_capitalized(match: re.Match):
    return f'<p class="capitalized">{m.group(2)}{m.group(3)}'


def capitalized(html: str):
    """Notation for marking paragraphs as having a first capital letter.
    
    Marquedown:
        [T]o be or not to be, that is the question.

    HTML:
        <p class="capitalized">
            To be or not to be, that is the question.
        </p>


    CSS can then be applied to format the first letter to be bigger
    or with a different font, to make it stand out.
    Ex.
        p.capitalized:first-letter {
            font-size: 3rem;
            font-weight: bold;
        }
    """

    return RE_CAPITALIZED.sub(_repl_capitalized, html)