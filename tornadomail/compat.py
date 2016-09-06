
"""
Python 2 and 3 object compatibility module.
"""

import sys


__all__ = ['unicode', 'basestring', 'StringIO', 'range', 'encode_base64']


if sys.version_info.major == 3:
    PY3 = True
else:
    PY3 = False


if PY3:
    basestring = str
    range = range
    unicode = str
    from email.base64mime import body_encode as encode_base64
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO
else:
    basestring = basestring
    range = xrange
    unicode = unicode
    from email.base64mime import encode as encode_base64
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
