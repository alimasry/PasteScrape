import requests
from bs4 import BeautifulSoup
from languages import *

class PasteScrape:
    """Scrap pastes from Pastebin.

    Parameters:
    -----------
    url : str
        The url of the paste to be scraped.

    Attributes:
    -----------
    id : string
        The id of the paste.
    lang : string
        The language used to highlight the text in the paste.
    data : list
        The text in the paste (each element represent a line).

    Methods:
    --------
    print()
        Print the text of the paste on the screen.
    write()
        Write the text of the paste in a file.
    get()
        Return the text of the paste in a string
    __get_id(url)
        Return the id of the paste given its url.
    """
    def __init__(self, url):
        
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # get the id of the paste
        self.id = self.__get_id(url)

        # detect the syntax highlighting
        lang = soup.find_all(class_='buttonsm')
        self.lang = get_lang(lang[len(lang) - 1].text, self.id)

        # get the text
        self.data = soup.find_all(True, {'class' : ['de1', 'de2']})

    def print(self):
        """Print the Text of the paste."""

        for line in self.data:
            print(line.text)

    def write(self):
        """Write the the text of the paste in a file."""

        for line in self.data:
            self.lang.file.write(line.text + '\n')

    def get(self):
        """Return the text of the paste in a string. """

        paste = ''
        for line in self.data:
            paste += line.text + '\n'
        return paste

    def __get_id(self, url):
        """Return the id of the paste.

        Parameters:
        -----------
        url : str
            The url of the paste to be scraped.
        """

        ind = 0
        for i in range(len(url)):
            if url[i] == '/':
                ind = i + 1
        return url[ind:]
