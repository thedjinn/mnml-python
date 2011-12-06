import re
import itertools

from cStringIO import StringIO

from node import Node

TAGNAME_REGEX = re.compile("[a-zA-Z_][a-zA-Z0-9_]*")
ARGUMENT_REGEX = re.compile("\s+([a-zA-Z_][a-zA-Z0-9_]*)=([^\s\"]+|\"(?:\\\\\"|[^\"])*\")")
HEREDOC_REGEX = re.compile("\s+->\s*$")

def add_lookahead(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip_longest(a, b)

def add_indent(iterable):
    last_indent = 0

    for line in iterable:
        stripped_line = line.lstrip(" ")

        if len(line) == 0:
            indent = last_indent
        else:
            indent = len(line) - len(stripped_line)
            last_indent = indent

        yield indent, stripped_line

def filter_comments(iterable):
    return ((indent, line) for indent, line in iterable if (len(line) > 0 and line[0] != "#") or len(line) == 0)

def parse_heredoc(iterable, root_indent):
    base_indent = None
    output = StringIO()

    for (current_indent, current_line), lookahead in iterable:
        base_indent = base_indent or current_indent

        if len(current_line) > 0:
            output.write((current_indent - base_indent) * " ")
            output.write(current_line)

        if not lookahead or lookahead[0] <= root_indent:
            break

        output.write("\n")

    return output.getvalue().rstrip()

def parse_document(iterable):
    stack = [(0, [])]

    for (current_indent, current_line), lookahead in iterable:
        match = TAGNAME_REGEX.match(current_line)
        if not match:
            continue

        pos = match.end()
        tag_name = match.group()
        arguments = {}

        while True:
            match = ARGUMENT_REGEX.match(current_line, pos)
            if not match:
                break

            key, value = match.groups()
            if value[0] == "\"":
                value = value[1:-1]
            arguments[key] = value
            pos = match.end()

        if HEREDOC_REGEX.match(current_line, pos):
            text = parse_heredoc(iterable, current_indent)
        else:
            text = current_line[pos:].strip()
            if len(text) == 0:
                text = None

        while current_indent < stack[-1][0]:
            stack.pop()

        if current_indent > stack[-1][0]:
            stack.append((current_indent, stack[-1][1][-1].children))

        node = Node(tag_name, arguments, text)
        stack[-1][1].append(node)

    return stack[0][1]

def parse_file(filename):
    with open(filename) as f:
        lines = (line.rstrip("\r\n") for line in f)
        prepared = add_lookahead(filter_comments(add_indent(lines)))
        return parse_document(prepared)

def parse_string(string):
    prepared = add_lookahead(filter_comments(add_indent(string.splitlines())))
    return parse_document(prepared)
