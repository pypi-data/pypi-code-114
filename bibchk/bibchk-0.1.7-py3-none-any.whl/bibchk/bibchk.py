##############################################################################
#           By
#                  ___                  _  __    _ _
#                 |   \ ___ _  _ __ _  | |/ /___| | |___ _ _
#                 | |) / _ \ || / _` | | ' </ -_) | / -_) '_|
#                 |___/\___/\_,_\__, | |_|\_\___|_|_\___|_|
#                               |___/
#                 
#           Please follow the licensing this work is under! Cheers!
##############################################################################

##############################################################################
# imports

from habanero import cn
import isbnlib
import argparse
import sys

##############################################################################
# doi

def bib_from_doi(doi):
    """Retrieves the BibTeX citation for a document with a given DOI.

    Parameters
    ----------
    doi : str
        The DOI string of the desired document.

    Returns
    -------
    bib : str
        The BibTeX citation of the given DOI.
    """
    
    try:
        doi_bib = cn.content_negotiation(ids=doi, format='bibtex')

    except:
        raise

    return doi_bib


def is_doi(url):
    """Check if a URL is a DOI URL.

    Parameters
    ----------
    url : str
        Potential DOI URL.

    Returns
    -------
    bool
        True if it is a DOI URL, False if not.
    """

    try:
        cn.content_negotiation(ids=url)
        return True

    except:
        return False

##############################################################################
# isbn

def get_isbn13(isbn_gen_str):
    """Returns a clean ISBN number if one exists in the given argument.

    Parameters
    ----------
    isbn_gen_str : str
        Potentially "dirty" string containing an ISBN number, possibly embedded in an URL.

    Returns
    -------
    isbn13 : str
        ISBN 13 number
    """

    isbn_like = isbnlib.get_isbnlike(isbn_gen_str, level='loose')[-1]  # Get ISBN from a URL or ISBN string.
    clean_isbn_like = isbnlib.clean(isbn_like)

    if isbnlib.is_isbn10(clean_isbn_like):  # Check if the ISBN is ISBN10 and changing it to ISBN13 if it is.
        isbn13 = isbnlib.to_isbn13(clean_isbn_like)
    else:
        isbn13 = clean_isbn_like

    return isbn13


def bib_from_isbn(isbn13):
    """Retrieves the BibTeX citation for a document with a given ISBN-13.

    Parameters
    ----------
    isbn : str
        The ISBN-13 number of the desired document.

    Returns
    -------
    bib : str
        The BibTeX citation of the given ISBN-13.
    """
    
    try:
        isbn_dict = isbnlib.meta(isbn13)
        isbn_bib = isbnlib.registry.bibformatters['bibtex'](isbn_dict)

    except:
        raise

    return isbn_bib


def is_isbn(url):
    """Check if the given URL has an ISBN

    Parameters
    ----------
    url : str
        URL with potential ISBN.

    Returns
    -------
    bool
        True if there is an ISBN, False if not.
    """

    return not isbnlib.notisbn(url)

##############################################################################
# cli

def get_bib(work_id):
    """Returns a BibTeX string if given a DOI or ISBN; returns None if it is not.

    Parameters
    ----------
    work_id : str
        String containing a potential work reference.

    Returns
    -------
    bib_str : str
        BibTeX string.
    """

    if is_doi(work_id):
        return bib_from_doi(work_id)

    elif is_isbn(work_id):
        return bib_from_isbn(work_id)

    else:
        return None

def print_bib(work_id, bib_str):
    """Prints BibTeX string.
    """

    if bib_str:
        print(bib_str + '\n')
    else:
        print(work_id + ' not a valid DOI or ISBN\n')


def parse_args(args):
    """Argument parser: takes IDs (DOIs or ISBNs) and returns BibTeX strings.

    Parameters
    ----------
    args : list
        List of arguments.

    Returns
    -------
    bib_dict : dict
        Dictionary of BibTeX strings.
    """

    parser = argparse.ArgumentParser('bibchk')
    parser.add_argument('IDs', nargs='+', type=str, help='DOIs or ISBNs')
    parsed = parser.parse_args(args)

    bib_dict = {}
    for ID in parsed.IDs:
        bib_dict[ID] = get_bib(ID)

    return bib_dict

##############################################################################
# main

def main():
    bib_dict = parse_args(sys.argv[1::])
    
    for ID in bib_dict.keys():
        print_bib(ID, bib_dict[ID])


if __name__ == '__main__':
    main()
