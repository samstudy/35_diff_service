# The code was taken and modified from http://www.aaronsw.com/2002/diff/diff.py

import difflib
import string


def isTag(x):
    return x[0] == "<" and x[-1] == ">"


def get_target_html(tag, a, b):
    out = []
    if tag[0] == "replace":
            out.append('< del class="diff modified">'+''.join(a[e[1]:e[2]]) +
                       '</del><ins class="diff modified">' +
                       ''.join(b[tag[3]:tag[4]])+"</ins>")
    if tag[0] == "delete":
            out.append('<span class="deleted_element">' +
                       ''.join(a[tag[1]:tag[2]]) + "</span>")
    if tag[0] == "insert":
            out.append('<span class="added_element">' +
                       ''.join(b[tag[3]:tag[4]]) + "</span>")
    else:
        if tag[1] == tag[3] and tag[2] == tag[4]:
                out.append(''.join(b[tag[3]:tag[4]]))
        else:
            out.append('<span class="moved_element">' +
                       ''.join(b[tag[3]:tag[4]]) + "</span>")
            out.append('<span class="deleted_element">' +
                       ''.join(b[tag[3]:tag[4]]) + "</span>")
    return ''.join(out)


def textDiff(a, b):
    out = []
    """Takes in strings a and b and returns a human-readable HTML diff."""
    try:
        matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    except TypeError:
        matcher = difflib.SequenceMatcher(None, a, b)
    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag in matcher.get_opcodes():
        ready_html = get_target_html(tag, a, b)
        out.append(ready_html)
    return ''.join(out)
