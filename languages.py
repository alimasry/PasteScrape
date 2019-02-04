def get_lang(lang, id):
    """Return the language used for highlighting the text.

    Parameters:
    -----------
    lang : str
        The language used to highlight the text in the paste.
    id : str
        Id of the paste to be scraped.
    """

    if lang == 'C++':
        return cpp(id)

    elif lang == 'C':
        return C(id)

    elif lang == 'C#':
        return Cs(id)

    elif lang == 'Java':
        return Java(id)

    elif lang == 'Python':
        return Python(id)

    elif lang == 'Html':
        return Html(id)

    elif lang == 'Css':
        return Css(id)

    else:
        return Text(id)

# available languages


class cpp:
    def __init__(self, id = ''):
        """Open .cpp file."""

        self.file = open(str(id) + '.cpp', 'w+')

class C:
    def __init__(self, id = ''):
        """Open .c file."""

        self.file = open(str(id) + '.c', 'w+')

class Cs:
    def __init__(self, id = ''):
        """Open .cs file."""

        self.file = open(str(id) + '.cs', 'w+')

class Java:
    def __init__(self, id = ''):
        """Open .java file."""

        self.file = open(str(id) + '.java', 'w+')

class Python:
    def __init__(self, id = ''):
        """Open .py file."""

        self.file = open(str(id) + '.py', 'w+')

class Html:
    def __init__(self, id = ''):
        """Open .html file."""

        self.file = open(str(id) + '.html', 'w+')

class Css:
    def __init__(self, id = ''):
        """Open .css file."""

        self.file = open(str(id) + '.css', 'w+')

class Text:
    def __init__(self, id = ''):
        """Open .txt file."""

        self.file = open(str(id) + '.txt', 'w+')
