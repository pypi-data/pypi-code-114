import re
import markdown


RE_CITATION = re.compile(r'^(?:\.+\n)?((?:\>.*\n)+)\n?\-{2}[ ](.+)(?:\n\'+)?', flags=re.MULTILINE)


def _repl_citation(match: re.Match):
    quote, source = match.group(1, 2)
    
    # Remove angle brackets and adjust indentation
    quote = '\n'.join('\t\t' + line[1:].lstrip() for line in quote.splitlines())

    # Put everything into HTML
    return f'<blockquote>\n\t<p>\n{quote}\n\t</p>\n\t<cite>{source}</cite>\n</blockquote>'


def citation(document: str):
    """Notation for blockquotes that include citation.

    Marquedown:
        ......................................................
        > You have enemies? Good. That means you've stood up
        > for something, sometime in your life.
        -- Winston Churchill
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''

    HTML:
        <blockquote>
            <p>
                You have enemies? Good. That means you've stood up
                for something, sometime in your life.
            </p>
            <cite>Winston Churchill</cite>
        </blockquote>
    """

    return RE_CITATION.sub(_repl_citation, document)