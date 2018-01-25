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
    # autojunk can cause malformed HTML, but also speeds up processing.
    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag in matcher.get_opcodes():
        if tag[0] == "replace":
            # @@ need to do something more complicated here
            # call textDiff but not for html, but for some html... ugh
            # gonna cop-out for now
            out.append('< del class="diff modified">'+''.join(a[e[1]:e[2]]) +
                       '</del><ins class="diff modified">' +
                       ''.join(b[tag[3]:tag[4]])+"</ins>")
        elif tag[0] == "delete":
            out.append('<span class="deleted_element">' +
                       ''.join(a[tag[1]:tag[2]]) + "</span>")
        elif tag[0] == "insert":
            out.append('<span class="added_element">' +
                       ''.join(b[tag[3]:tag[4]]) + "</span>")
        elif tag[0] == "equal":
            if tag[1] == tag[3] and tag[2] == tag[4]:
                out.append(''.join(b[tag[3]:tag[4]]))
            else:
                out.append('<span class="moved_element">' +
                           ''.join(b[tag[3]:tag[4]]) + "</span>")
                out.append('<span class="deleted_element">' +
                           ''.join(b[tag[3]:tag[4]]) + "</span>")
        else:
            raise "Um, something's broken. I didn't expect a '" + tag[0] + "'."
    return ''.join(out)
