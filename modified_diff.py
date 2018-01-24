#!/usr/bin/python
"""HTML Diff: http://www.aaronsw.com/2002/diff
Rough code, badly documented. Send me comments and patches."""

__author__ = 'Aaron Swartz <me@aaronsw.com>'
__copyright__ = '(C) 2003 Aaron Swartz. GNU GPL 2 or 3.'
__version__ = '0.22'

import difflib
import string


def textDiff(a, b):
    out = []
    """Takes in strings a and b and returns a human-readable HTML diff."""
    try:  # autojunk can cause malformed HTML, but also speeds up processing.
        s = difflib.SequenceMatcher(None, a, b, autojunk=False)
    except TypeError:
        s = difflib.SequenceMatcher(None, a, b)
    for e in s.get_opcodes():
        if e[0] == "replace":
            # @@ need to do something more complicated here
            # call textDiff but not for html, but for some html... ugh
            # gonna cop-out for now
            out.append('< del class="diff modified">'+''.join(a[e[1]:e[2]]) +
                       '</del><ins class="diff modified">' +
                       ''.join(b[e[3]:e[4]])+"</ins>")
        elif e[0] == "delete":
            out.append('<span class="deleted_element">' +
                       ''.join(a[e[1]:e[2]]) + "</span>")
        elif e[0] == "insert":
            out.append('<span class="added_element">' +
                       ''.join(b[e[3]:e[4]]) + "</span>")
        elif e[0] == "equal":
            if e[1] == e[3] and e[2] == e[4]:
                out.append(''.join(b[e[3]:e[4]]))
            else:
                out.append('<span class="moved_element">' +
                           ''.join(b[e[3]:e[4]]) + "</span>")
                out.append('<span class="deleted_element">' +
                           ''.join(b[e[3]:e[4]]) + "</span>")
        else:
            raise "Um, something's broken. I didn't expect a '" + e[0] + "'."
    return ''.join(out)
