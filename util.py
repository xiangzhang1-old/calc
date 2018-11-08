# -*- coding: utf-8 -*-
"""Implement constants and utility functions."""
from __future__ import print_function, division, unicode_literals
import re
import unicodedata


def slugify(value):
    """
    Turns a string into a valid filename.

    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.

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
