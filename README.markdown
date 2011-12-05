# Python Mnml parser

This Python package contains a parser for Mmml documents.

For more information on the Mnml language see the [JavaScript Mnml parser
readme](https://github.com/thedjinn/mnml) or
[getmnml.com](http://getmnml.com).

## Installation

The parser is available as a Pip package:

    pip install mnml

Alternatively, to install from the git repository: (you may need to sudo
depending on your Python environment)

    python setup.py install

## Usage

After installation the Mnml parser can be used to parse either files or
strings. Either way, you need to import the module first:

    import mnml

### Parsing files

To parse files you can use the `parse_file` function. This function requires
a filename to parse.

    document = mnml.parse_file("example.mnml")

### Parsing strings

Parsing a Mnml document that is contained in a string is just as easy. In this
case the `parse_string` function is used.

    document = mnml.parse_string(mnml_file)

### Document structure

Both Mnml parsing functions return an array containing all tags at the root
level. These tags itself (and theirs children) are represented as instances of
the `Node` class.

The `Node` class has the following properties:

 - `name`: A string containing the name of the tag.
 - `args`: A dictionary containing the arguments of the tag. All keys and
   values are represented as strings.
 - `text`: The text node of the tag. This is either a string or `None` if no
   text was given.
 - `children`: An array of `Node` instances representing the children of this
   tag. When there are no children this is an empty array.

## Contribute

If you found a bug, don't hesitate to make a pull request.

## License

Copyright (c) 2011 [Emil Loer](http://emilloer.com).

Permission  is  hereby granted, free of charge, to any person obtaining a copy of  this  software  and  associated  documentation files  (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is  furnished to do so, subject to the following conditions:

The  above  copyright  notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF  ANY  KIND, EXPRESS  OR  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE  AND  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER  IN  AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  THE SOFTWARE.
