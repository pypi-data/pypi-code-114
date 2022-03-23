import random
from hashlib import sha256
import base64
from math import sqrt
from getpass import getpass

# globals

N_CHARS_DEF = 6
# default Base 64 n_characters
# if is 6 then there are 64^6 = 68,719,476,736 possible values
# will be sufficient if there are less than a billion or so tokens
# in second list so that hash collisions won't significantly affect
# the overlap percentage for reason samples

SEED = 7626472
# default random seed for sampling first list
# set to None for non-repeatable result or anything else
# to get a different sample

N_MIN = 5
# Minimum number of characters in salt if received through prompt


def get_salt():
    """
    Prompt for password or salt
    ensure exceeds minimum length
    :return:
    """
    salt = getpass('Password salt:')
    assert len(salt) >= N_MIN
    return salt


def hash_string_base64(string, salt, n_chars=N_CHARS_DEF):
    """
    :param string: any string
    :param salt: password used for salting before hash
    :param n_chars: number of characters used in the hash,
        default is 6 (base64, os each char can code for 64 items)
        increase to 8 or if you have billions of tokens and want to
        avoid collisions
    :return: a Base64 hash string (i.e. upper and lowercase, numerals
        and + and / (count them, there are 64 unique chars)
    """
    salted = str(string) + salt
    hashed = sha256(salted.encode('utf-8')).digest()
    b64 = base64.b64encode(hashed)
    return b64[0:n_chars].decode()


def create_blob(item_set, n_samples, seed=SEED, n_chars=N_CHARS_DEF, salt=None):
    """
    Use this for coding the blob hash in the first set of tokens
    :param item_set: items in the first set
        (will be coerced into string type)
    :param n_samples: number of samples to choose
    :param seed: random seed used for choosing sample,
        default is a fixed one, can use None for random, non-repeatable
        sampling
    :param n_chars: number of characters used in the hash,
        default is 6 (base64, os each char can code for 64 items)
        increase to 8 or if you have billions of tokens and want to
        avoid collisions
    :param salt: password or salt string used in the hash, provides for
        scripting or testing but more secure to not provide and type in
        at the prompt
    :return: blob (a character string of Base64 hashes, joined together)
    """
    if salt is None:
        salt = get_salt()

    random.seed(seed)
    items = item_set.copy()
    random.shuffle(items)
    items = items[0: n_samples]

    max_num = 64**n_chars

    # print reminder of max tokens for about a 1% chance of having a
    # collision on any query

    max_tokens = max_num/100
    max_tokens_millions = int(max_tokens/1e6)
    print('n_chars=%s, good for up to %s million tokens' % (n_chars, max_tokens_millions))

    hashes = [hash_string_base64(str(i), salt, n_chars=n_chars) for i in items]
    return ''.join(hashes)


def split_blob(blob, n_chars=N_CHARS_DEF):
    """
    Split the blob into a list of n_char long hashes
    :param blob: the blob hash
    :param n_chars: number of characters used to create it
    :return: list of n_char long hashes
    """
    num = len(blob)/n_chars
    assert num == int(num)
    num = int(num)
    return [blob[i*n_chars:i*n_chars+n_chars] for i in range(num)]


def check_other_list(blob, other_list, n_chars=N_CHARS_DEF, salt=None):
    """
    Returns list of Booleans which is True if hashes split from blob
    are in the hashes of the second list
    :param blob: the blob of hashes
    :param other_list: the list of other tokens (not yet hashed)
    :param n_chars: the number of characters for the hashes
    :param salt: the password or salt, will prompt if not given
        must be same as the one used to create the blob or no overlap
        will be found (or possibly a few hash collisions)
    :return:
    """

    if salt is None:
        salt = get_salt()

    other_hashes = [hash_string_base64(str(i), salt, n_chars=n_chars) for i in other_list]
    other_hashes = set(other_hashes)

    hash_items = split_blob(blob, n_chars=n_chars)
    return [hash_item in other_hashes for hash_item in hash_items]


def check_overlap(blob, other_list, n_chars=N_CHARS_DEF, salt=None):
    """
    From the blob of sampled hashes from the first list,
    determine the percentage of them that are in the second list.
    :param blob: blob created by create_blob
        (a character string of Base64 hashes, joined together)
    :param other_list: list of the other tokens
        (will be coerced into string type)
    :param n_chars: number of characters used in the hash,
        default is 6 (base64, os each char can code for 64 items)
        increase to 8 or if you have billions of tokens and want to
        avoid collisions
        Must be the same used to create the blob
    :param salt: password or salt string used in the hash, provides for
        scripting or testing but more secure to not provide and type in
        at the prompt
        Must be the same used to create blob or there will likely be
        no overlap (unless an unlucky hash collision).
        Will warn about this if there are no overlaps found.
    :return:
    """
    checks = check_other_list(blob, other_list, n_chars=n_chars, salt=salt)

    n_intersect = sum(checks)
    n_tot = len(checks)

    q = (n_tot-n_intersect)/n_tot
    n_int_error = sqrt(n_intersect * q)

    print('Intersection: %s +/- %s' % (n_intersect, round(n_int_error)))

    fraction = n_intersect/n_tot
    fraction_err = n_int_error/n_tot

    perc = 100.0 * fraction
    perc_err = 100 * fraction_err

    print('Percent intersect: %0.2f +/- %0.2f' % (perc, perc_err))

    if n_intersect == 0:
        print('\n(Wrong password or different n_chars?)')

    return perc, perc_err
