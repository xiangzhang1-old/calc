"""Implements constants and utility functions/classes."""
from __future__ import print_function, division, unicode_literals
import re, unicodedata, pandas as pd, os


script_dir = os.path.dirname(os.path.realpath(__file__))


def slugify(value):
    r"""
    Make a string URL- and filename-friendly.

    Normalizes string into unicode, converts to lowercase, removes non-alpha-nu-
    merics, and converts spaces to hyphens.

    Taken from django/utils/text.py. In Django, a "slug" is a URL- and filename-
    friendly string.

    :param unicode value: String to be converted
    :return: Filename-friendly string
    :rtype: unicode
    :raises TypeError: if value is not unicode string

    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('[-\s]+', '-', value))
    return value


periodic_table = pd.read_excel(script_dir + '/periodic_table.xlsx')
r"""
Periodic table. :class:`pandas.DataFrame` read from periodic_table.xlsx.
"""
